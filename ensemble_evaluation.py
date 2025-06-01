import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from collections import Counter


def evaluate_models(return_details=False):
    df = pd.read_csv("preprocessed_data.csv")
    X_text = df["cleaned_text"]
    y_true = df["predicted_sentiment"]

    # Load models and vectorizers
    models = [
        joblib.load("model1.pkl"),
        joblib.load("model2.pkl"),
        joblib.load("model3.pkl")
    ]
    vectorizers = [
        joblib.load("vectorizer1.pkl"),
        joblib.load("vectorizer2.pkl"),
        joblib.load("vectorizer3.pkl")
    ]

    # Predict and perform majority voting
    def get_majority_vote(text):
        preds = []
        for model, vec in zip(models, vectorizers):
            x_vec = vec.transform([text])
            pred = model.predict(x_vec)[0]
            preds.append(pred)
        return Counter(preds).most_common(1)[0][0]

    ensemble_preds = [get_majority_vote(text) for text in X_text]

    # Evaluation
    acc = accuracy_score(y_true, ensemble_preds)
    confusion = confusion_matrix(y_true, ensemble_preds)
    report = classification_report(y_true, ensemble_preds)
    label_counts = Counter(ensemble_preds)

    # Save results
    joblib.dump((acc, report, confusion), "evaluation_results.pkl")

    if return_details:
        return acc, list(y_true), ensemble_preds, label_counts
    return f"Ensemble Accuracy: {acc*100:.2f}%\nConfusion Matrix:\n{confusion}\nClassification Report:\n{report}"
