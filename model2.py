import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model2():
    df = pd.read_csv("data_part2.csv")

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["cleaned_text"])
    y = df["predicted_sentiment"]

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, "model2.pkl")
    joblib.dump(vectorizer, "vectorizer2.pkl")

    return "Model 2 training complete."