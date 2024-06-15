# app.py

import streamlit as st
import requests
import spacy
import re
import joblib
from data_retrieval import get_movie_info
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from train_nlp_model import preprocess

# Load intent classifier
pipeline = joblib.load('intent_classifier.pkl')

# Streamlit app
def main():
    st.title('Hindi Film Industry Chatbot')

    # User input textbox
    user_input = st.text_input('Enter your question about the Hindi film industry')

    # Button to send query
    if st.button('Submit'):
        if user_input:
            # Preprocess user input
            processed_input = preprocess(user_input)

            # Predict intent using trained model
            intent = pipeline.predict([processed_input])[0]

            # Generate response based on intent
            if intent == 'get_movie_info':
                # Extract movie name from user input (you may need more robust entity extraction logic)
                movie_name = re.search(r'about (.+?)$', user_input.lower()).group(1).strip()
                
                # Fetch movie information
                movie_info = get_movie_info(movie_name)

                if movie_info:
                    # Display relevant movie information
                    response = f"Here's what I found about {movie_name}: {movie_info['extract']}"
                else:
                    response = f"I'm sorry, I couldn't find information about {movie_name}."
            else:
                response = "I'm sorry, I don't have information on that topic right now."

            # Display response
            st.markdown(f'**Response:** {response}')

if __name__ == '__main__':
    main()
