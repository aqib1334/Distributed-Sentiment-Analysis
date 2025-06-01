import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model1():
    # Load part1
    df = pd.read_csv("data_part1.csv")

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["cleaned_text"])
    y = df["predicted_sentiment"]

    model = RandomForestClassifier()
    model.fit(X, y)

    # Save model and vectorizer
    joblib.dump(model, "model1.pkl")
    joblib.dump(vectorizer, "vectorizer1.pkl")

    return "Model 1 training complete."