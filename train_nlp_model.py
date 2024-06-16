from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import re

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
        "Who gave the music direction for PK?",
        "Who is the director of Dangal?",
        "Tell me the awards won by 3 Idiots"
    ],
    'intent': [
        "get_movie_info",
        "get_actor_info",
        "get_box_office",
        "get_controversies",
        "get_actor_info",
        "get_release_year",
        "get_best_actor",
        "get_music_direction",
        "get_director",
        "get_awards"
    ]
}

# Preprocess the text data
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

# Split data
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
