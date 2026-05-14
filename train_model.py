import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from utils.preprocess import clean_text

# Load dataset
df = pd.read_csv("resume_dataset.csv")

# Clean text
df['cleaned_resume'] = df['resume_text'].apply(clean_text)

# Features and labels
X = df['cleaned_resume']
y = df['category']

# TF-IDF
tfidf = TfidfVectorizer()

X_vectorized = tfidf.fit_transform(X)

# Train model
model = LogisticRegression()

model.fit(X_vectorized, y)

# Save model
joblib.dump(model, 'model.pkl')

# Save vectorizer
joblib.dump(tfidf, 'tfidf.pkl')

print("Model Trained Successfully")


python train_model.py
