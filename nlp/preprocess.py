import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

nltk.download('stopwords')

stop_words = set(stopwords.words('portuguese'))

stemmer = RSLPStemmer()

def preprocess_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zà-ú\s]', '', text)

    tokens = text.split()

    tokens = [t for t in tokens if t not in stop_words]

    tokens = [stemmer.stem(t) for t in tokens]

    return " ".join(tokens)