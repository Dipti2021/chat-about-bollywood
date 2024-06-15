# train_nlp_model.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import re

# Define preprocess function
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

# Sample data for intents
data = {
    'text': [
        "Tell me about Dangal",
        "Who acted in 3 Idiots?",
        "What was the box office collection of PK?",
        "What controversies surrounded Padmaavat?",
        "Who is the actor of PK?",
        "When was Dangal released?",
        "Who won the Best Actor award for 3 Idiots?",
        "Who gave the music direction for PK?"
    ],
    'intent': [
        "get_movie_info",
        "get_actor_info",
        "get_box_office",
        "get_controversies",
        "get_actor_info",
        "get_release_year",
        "get_best_actor",
        "get_music_direction"
    ]
}

# Preprocess the text data
X = [preprocess(text) for text in data['text']]
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

print("Model trained and saved successfully.")
