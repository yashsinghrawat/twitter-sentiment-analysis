🔥 Twitter Sentiment Analysis Engine

A production-ready Natural Language Processing system that classifies tweets into Positive or Negative sentiment in real time.

Built using classical NLP techniques and deployed as an interactive web application.

👉 Live App: (Paste your Streamlit link here)

⭐ Overview

This project implements an end-to-end machine learning pipeline for sentiment classification on Twitter data.
It transforms raw tweets into meaningful predictions using TF-IDF vectorization and Logistic Regression.

The system is optimized for:

Real-time inference

Clean preprocessing

High interpretability

Lightweight deployment

Unlike deep learning-heavy solutions, this architecture prioritizes speed, explainability, and production simplicity.

🧠 Key Features

✅ End-to-end ML pipeline
✅ Tweet-specific preprocessing
✅ TF-IDF feature engineering with n-grams
✅ Logistic Regression classifier
✅ Probability-based predictions
✅ Interactive Streamlit UI
✅ Fully deployed cloud application

⚙️ Tech Stack

Machine Learning

Scikit-learn

TF-IDF Vectorizer

Logistic Regression

Backend / Deployment

Streamlit

Python 3.11

Tools

GitHub

PyCharm

📊 Model Performance
Metric	Score
Accuracy	76.4%
F1 Score	0.76

Achieved strong performance despite the noisy and highly unstructured nature of Twitter data.

🔍 Dataset

Sentiment140 Dataset

1.6 million labeled tweets

Binary sentiment labels

Real-world social media noise

This makes the model robust for practical NLP scenarios.

🏗️ ML Pipeline
Raw Tweets
   ↓
Text Cleaning (URLs, mentions, punctuation removal)
   ↓
TF-IDF Vectorization (1–2 grams)
   ↓
Logistic Regression
   ↓
Real-Time Sentiment Prediction

🚀 Deployment

The model is deployed using Streamlit Community Cloud, enabling users to analyze sentiment instantly through a browser interface.

This demonstrates the transition from:

👉 Notebook experimentation
→ Production-style ML system.

💡 Why This Project Matters

Most ML projects stop at training.

This project goes further by focusing on shipping a usable product.

It highlights practical engineering skills such as:

Model serialization

Dependency management

Environment setup

Cloud deployment

UI integration

🔮 Future Improvements

Transformer-based sentiment models (BERT / DistilBERT)

Real-time tweet ingestion

Multi-class sentiment (Positive / Neutral / Negative)

Docker containerization

CI/CD pipeline

👨‍💻 Author

Yash Rawat

If you found this project interesting, feel free to connect!
