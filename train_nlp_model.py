# train_nlp_model.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import re

# Sample data for intents
data = {
    'text': ["Tell me about Dangal", "Who acted in 3 Idiots?", "What was the box office collection of PK?", "What controversies surrounded Padmaavat?"],
    'intent': ["get_movie_info", "get_actor_info", "get_box_office", "get_controversies"]
}

# Preprocess the text data
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

# Split data
X = data['text']
y = data['intent']

# Initialize vectorizer and classifier
vectorizer = TfidfVectorizer()
classifier = LogisticRegression()

# Create pipeline
pipeline = Pipeline([
    ('vectorizer', vectorizer),
    ('classifier', classifier),
])

# Train the model
pipeline.fit(X, y)

# Save the trained model
joblib.dump(pipeline, 'intent_classifier.pkl')
