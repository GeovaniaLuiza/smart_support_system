# ==========================================================
# TREINAMENTO DO MODELO DE IA — PLN + NAIVE BAYES
# ==========================================================
#
# Este módulo é responsável pelo treinamento do modelo
# de classificação de sentimentos utilizado no sistema.
#
# Objetivo:
# Criar um modelo de Inteligência Artificial capaz de
# identificar sentimentos em mensagens textuais.
#
# Classes previstas:
#
# - Positivo
# - Negativo
# - Neutro
#
# Técnicas utilizadas:
#
# ✔ Processamento de Linguagem Natural (PLN)
# ✔ Vetorização TF-IDF
# ✔ Naive Bayes Multinomial
# ✔ Balanceamento de classes
# ✔ Machine Learning supervisionado
#
# ==========================================================



# ==========================================================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ==========================================================

# Biblioteca para manipulação de tabelas/dados
import pandas as pd

# Biblioteca para salvar o modelo treinado
import pickle


# ==========================================================
# FERRAMENTAS DE MACHINE LEARNING
# ==========================================================

# Divisão treino/teste
from sklearn.model_selection import train_test_split


# Pipeline de processamento
#
# Permite combinar:
# - vetorização
# - modelo de IA
#
from sklearn.pipeline import Pipeline


# Vetorização TF-IDF
#
# Converte texto em representação numérica.
#
from sklearn.feature_extraction.text import TfidfVectorizer


# Algoritmo de classificação
#
# Naive Bayes Multinomial é eficiente para textos.
#
from sklearn.naive_bayes import MultinomialNB


# Métricas de avaliação do modelo
from sklearn.metrics import classification_report


# Técnica de balanceamento
from sklearn.utils import resample


# Função de pré-processamento criada no projeto
from nlp.preprocess import preprocess_text



# ==========================================================
# CARREGAMENTO DO DATASET
# ==========================================================
#
# Dataset utilizado:
# Tweets de companhias aéreas (Kaggle)
#
# O dataset contém mensagens já rotuladas
# com sentimentos.
#
# ==========================================================

df = pd.read_csv("data/Tweets.csv")



# ==========================================================
# SELEÇÃO DAS COLUNAS IMPORTANTES
# ==========================================================
#
# text                -> mensagem textual
# airline_sentiment   -> sentimento da mensagem
#
# dropna():
# remove valores nulos.
#
# ==========================================================

df = df[['text', 'airline_sentiment']].dropna()



# ==========================================================
# RENOMEAÇÃO DAS COLUNAS
# ==========================================================
#
# Facilita a leitura do código.
#
# ==========================================================

df.columns = ['message', 'sentiment']



# ==========================================================
# BALANCEAMENTO DAS CLASSES
# ==========================================================
#
# Problema:
# datasets reais geralmente possuem classes
# desbalanceadas.
#
# Isso pode causar viés no modelo.
#
# Solução:
# aplicar oversampling com resample().
#
# ==========================================================


# ----------------------------------------------------------
# Separação das classes
# ----------------------------------------------------------

df_negative = df[df.sentiment == "negative"]

df_neutral = df[df.sentiment == "neutral"]

df_positive = df[df.sentiment == "positive"]



# ----------------------------------------------------------
# Descobre o tamanho da maior classe
# ----------------------------------------------------------

max_size = max(
    len(df_negative),
    len(df_neutral),
    len(df_positive)
)



# ----------------------------------------------------------
# Oversampling
#
# replace=True:
# permite repetir amostras.
#
# random_state:
# garante reprodutibilidade.
#
# ----------------------------------------------------------

df_negative = resample(
    df_negative,
    replace=True,
    n_samples=max_size,
    random_state=42
)

df_neutral = resample(
    df_neutral,
    replace=True,
    n_samples=max_size,
    random_state=42
)

df_positive = resample(
    df_positive,
    replace=True,
    n_samples=max_size,
    random_state=42
)



# ==========================================================
# CONCATENAÇÃO DAS CLASSES BALANCEADAS
# ==========================================================

df = pd.concat([
    df_negative,
    df_neutral,
    df_positive
])



# ==========================================================
# PRÉ-PROCESSAMENTO DOS TEXTOS
# ==========================================================
#
# Cada mensagem passa pelas etapas:
#
# - limpeza textual
# - tokenização
# - remoção de stop words
# - stemming
#
# ==========================================================

df["processed"] = df["message"].apply(preprocess_text)



# ==========================================================
# DEFINIÇÃO DAS VARIÁVEIS
# ==========================================================
#
# X -> entradas (texto)
# y -> saídas (sentimentos)
#
# ==========================================================

X = df["processed"]

y = df["sentiment"]



# ==========================================================
# DIVISÃO TREINO / TESTE
# ==========================================================
#
# Objetivo:
# separar dados para:
#
# - treinamento
# - validação
#
# test_size=0.2:
# 20% para teste.
#
# stratify=y:
# mantém proporção das classes.
#
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)



# ==========================================================
# CONSTRUÇÃO DO MODELO
# ==========================================================
#
# Pipeline utilizada:
#
# 1) TF-IDF
# 2) Naive Bayes
#
# ==========================================================

model = Pipeline([

    # ------------------------------------------------------
    # ETAPA 1 — TF-IDF
    # ------------------------------------------------------
    #
    # TF-IDF:
    # Term Frequency - Inverse Document Frequency
    #
    # Converte texto em números.
    #
    # ngram_range=(1,2):
    # usa unigramas e bigramas.
    #
    # max_features=8000:
    # limita vocabulário.
    #
    # ------------------------------------------------------

    ("tfidf", TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=8000
    )),


    # ------------------------------------------------------
    # ETAPA 2 — NAIVE BAYES
    # ------------------------------------------------------
    #
    # Algoritmo probabilístico baseado no Teorema
    # de Bayes.
    #
    # Muito eficiente para classificação textual.
    #
    # ------------------------------------------------------

    ("nb", MultinomialNB())
])



# ==========================================================
# TREINAMENTO DO MODELO
# ==========================================================
#
# O modelo aprende padrões existentes nos dados.
#
# ==========================================================

model.fit(X_train, y_train)



# ==========================================================
# REALIZAÇÃO DAS PREVISÕES
# ==========================================================

preds = model.predict(X_test)



# ==========================================================
# AVALIAÇÃO DO MODELO
# ==========================================================
#
# classification_report():
#
# Exibe:
#
# - precisão
# - recall
# - F1-score
# - acurácia
#
# ==========================================================

print("\n=== CLASSIFICATION REPORT ===")

print(classification_report(y_test, preds))



# ==========================================================
# SALVAMENTO DO MODELO TREINADO
# ==========================================================
#
# O modelo é salvo em arquivo .pkl
# para reutilização futura.
#
# ==========================================================

with open("nlp/sentiment_model.pkl", "wb") as f:

    pickle.dump(model, f)



# ==========================================================
# MENSAGEM DE CONFIRMAÇÃO
# ==========================================================

print("\nModelo treinado com dataset Kaggle e balanceado!")



# ==========================================================
# VERIFICAÇÃO FINAL DAS CLASSES
# ==========================================================
#
# Exibe a distribuição após balanceamento.
#
# ==========================================================

print("\nDistribuição final:")

print(df["sentiment"].value_counts())



# ==========================================================
# IMPORTÂNCIA NO PROJETO
# ==========================================================
#
# Este módulo representa a etapa de aprendizado
# do sistema inteligente.
#
# O modelo aprende padrões linguísticos presentes
# nos dados e posteriormente consegue classificar
# novas mensagens automaticamente.
#
# Relação com o trabalho:
#
# ✔ Inteligência Artificial
# ✔ Machine Learning
# ✔ PLN
# ✔ Naive Bayes
# ✔ Representação numérica de texto
# ✔ Tratamento de dados não estruturados
#
# ==========================================================