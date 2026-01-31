st.set_page_config(page_title="Twitter Sentiment Analyzer", page_icon="🔥")

import streamlit as st
import joblib
import re
import string

# Load model and vectorizer
model = joblib.load("twitter_sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

def clean_tweet(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text


st.title("Real-Time Twitter Sentiment Analysis")

tweet = st.text_area("Enter a Tweet")

if st.button("Analyze"):

    cleaned = clean_tweet(tweet)
    vectorized = vectorizer.transform([cleaned])

    prediction = model.predict(vectorized)[0]
    probability = model.predict_proba(vectorized)[0]

    if prediction == 1:
        st.success(f"Positive ✅ | Confidence: {probability[1]*100:.2f}%")
    else:
        st.error(f"Negative ❌ | Confidence: {probability[0]*100:.2f}%")
