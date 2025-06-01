import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model3():
    df = pd.read_csv("data_part3.csv")

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["cleaned_text"])
    y = df["predicted_sentiment"]

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, "model3.pkl")
    joblib.dump(vectorizer, "vectorizer3.pkl")

    return "Model 3 training complete."