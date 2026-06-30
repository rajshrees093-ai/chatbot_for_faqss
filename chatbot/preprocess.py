import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    tokens=word_tokenize(text)
    tokens=[
        word for word in tokens
        if word not in stop_words
        and word not in string.punctuation
    ]

    return " ".json(tokens)