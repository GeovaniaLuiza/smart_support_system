import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

from sklearn.utils import resample

from nlp.preprocess import preprocess_text

# =========================
# 📥 CARREGAR DATASET KAGGLE
# =========================

df = pd.read_csv("data/Tweets.csv")

df = df[['text', 'airline_sentiment']].dropna()

df.columns = ['message', 'sentiment']

# =========================
# ⚖️ BALANCEAMENTO (CORREÇÃO DO VIÉS)
# =========================

df_negative = df[df.sentiment == "negative"]
df_neutral = df[df.sentiment == "neutral"]
df_positive = df[df.sentiment == "positive"]

max_size = max(len(df_negative), len(df_neutral), len(df_positive))

df_negative = resample(df_negative, replace=True, n_samples=max_size, random_state=42)
df_neutral = resample(df_neutral, replace=True, n_samples=max_size, random_state=42)
df_positive = resample(df_positive, replace=True, n_samples=max_size, random_state=42)

df = pd.concat([df_negative, df_neutral, df_positive])

# =========================
# 🔧 PREPROCESSAMENTO
# =========================

df["processed"] = df["message"].apply(preprocess_text)

X = df["processed"]
y = df["sentiment"]

# =========================
# 🔀 TREINO / TESTE
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# 🤖 MODELO MELHORADO
# =========================

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=8000
    )),
    ("nb", MultinomialNB())
])

model.fit(X_train, y_train)

preds = model.predict(X_test)

# =========================
# 📊 AVALIAÇÃO
# =========================

print("\n=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, preds))

# =========================
# 💾 SALVAR MODELO
# =========================

with open("nlp/sentiment_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\nModelo treinado com dataset Kaggle e balanceado!")

# =========================
# 📊 CHECK FINAL
# =========================

print("\nDistribuição final:")
print(df["sentiment"].value_counts())