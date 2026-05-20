import pickle

from nlp.preprocess import preprocess_text

with open("nlp/sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_sentiment(text):

    processed = preprocess_text(text)

    prediction = model.predict([processed])[0]

    probabilities = model.predict_proba([processed])[0]

    confidence = max(probabilities)

    return prediction, confidence