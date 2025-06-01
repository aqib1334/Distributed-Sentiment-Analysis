import pandas as pd
import numpy as np
import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

nltk.download("stopwords")
nltk.download("wordnet")

def preprocess_data():
    # Load dataset
    df = pd.read_csv("balanced_sentiment_dataset_first.csv", encoding="ISO-8859-1")
    df.dropna(subset=["text", "sentiment"], inplace=True)

    # Preprocessing
    tokenizer = RegexpTokenizer(r'\w+')
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))

    def preprocess_text(text):
        text = re.sub(r"[^a-zA-Z\s]", "", str(text))
        tokens = tokenizer.tokenize(text.lower())
        tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
        return " ".join(tokens)

    df["cleaned_text"] = df["text"].apply(preprocess_text)

    # Drop rows where cleaned_text might still be empty
    df["cleaned_text"].replace("", np.nan, inplace=True)
    df.dropna(subset=["cleaned_text"], inplace=True)

    # Sentiment analysis
    def get_sentiment(text): 
        return TextBlob(text).sentiment.polarity

    def classify_sentiment(polarity): 
        if polarity > 0:
            return "positive"
        elif polarity < 0:
            return "negative"
        else:
            return "neutral"

    df["sentiment_polarity"] = df["cleaned_text"].apply(get_sentiment)
    df["predicted_sentiment"] = df["sentiment_polarity"].apply(classify_sentiment)

    # Keep necessary columns only
    df = df[["cleaned_text", "predicted_sentiment"]]

    # Save full preprocessed data
    df.to_csv("preprocessed_data.csv", index=False)

    # Split and save parts
    part1, part2, part3 = np.array_split(df.sample(frac=1, random_state=42), 3)
    part1.to_csv("data_part1.csv", index=False)
    part2.to_csv("data_part2.csv", index=False)
    part3.to_csv("data_part3.csv", index=False)

    return "✅ Preprocessing complete. Saved: data_part1.csv, data_part2.csv, data_part3.csv"