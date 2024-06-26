import streamlit as st
import joblib
import re
from data_retrieval import get_release_year, get_actors, get_director, get_awards
from train_nlp_model import preprocess

# Load intent classifier
pipeline = joblib.load('intent_classifier.pkl')

# Maintain conversation state
if 'conversation_context' not in st.session_state:
    st.session_state.conversation_context = {}

# Streamlit app
def main():
    st.title('Movie Chatbot')

    # User input textbox
    user_input = st.text_input('You:')

    # Button to send query
    if st.button('Send'):
        if user_input:
            try:
                # Preprocess user input
                processed_input = preprocess(user_input)

                # Predict intent using trained model
                intent = pipeline.predict([processed_input])[0]

                # Generate response based on intent
                if intent == 'get_movie_info':
                    # Extract movie name from user input
                    match = re.search(r'about (.+?)$', user_input.lower())
                    if match:
                        movie_name = match.group(1).strip()
                        # Fetch movie information
                        movie_info = get_movie_info(movie_name)
                        if movie_info:
                            response = f"Movie Bot: {movie_info['extract']}"
                            # Update conversation context
                            st.session_state.conversation_context['movie_info'] = movie_name
                        else:
                            response = f"Movie Bot: I'm sorry, I couldn't find information about {movie_name}."
                    else:
                        response = "Movie Bot: I'm sorry, I couldn't understand the movie name in your query."

                elif intent == 'get_release_year':
                    # Check if conversation context has movie_info
                    movie_name = get_movie_name_from_context_or_query(user_input, 'released')
                    if movie_name:
                        release_year = get_release_year(movie_name)
                        if release_year:
                            response = f"Movie Bot: The movie {movie_name} was released in {release_year}."
                        else:
                            response = f"Movie Bot: I'm sorry, I don't have information about when {movie_name} was released."
                    else:
                        response = "Movie Bot: Please provide a movie name first."

                elif intent == 'get_actor_info':
                    # Check if conversation context has movie_info
                    movie_name = get_movie_name_from_context_or_query(user_input, 'actors')
                    if movie_name:
                        actors = get_actors(movie_name)
                        if actors:
                            response = f"Movie Bot: The actors in {movie_name} are {', '.join(actors)}."
                        else:
                            response = f"Movie Bot: I'm sorry, I don't have information about the actors in {movie_name}."
                    else:
                        response = "Movie Bot: Please provide a movie name first."

                elif intent == 'get_director':
                    # Check if conversation context has movie_info
                    movie_name = get_movie_name_from_context_or_query(user_input, 'director')
                    if movie_name:
                        director = get_director(movie_name)
                        if director:
                            response = f"Movie Bot: The director of {movie_name} is {director}."
                        else:
                            response = f"Movie Bot: I'm sorry, I don't have information about the director of {movie_name}."
                    else:
                        response = "Movie Bot: Please provide a movie name first."

                elif intent == 'get_awards':
                    # Check if conversation context has movie_info
                    movie_name = get_movie_name_from_context_or_query(user_input, 'awards')
                    if movie_name:
                        awards = get_awards(movie_name)
                        if awards:
                            response = f"Movie Bot: Awards for {movie_name}: {awards}."
                        else:
                            response = f"Movie Bot: I'm sorry, I couldn't find awards information for {movie_name}."
                    else:
                        response = "Movie Bot: Please provide a movie name first."

                else:
                    response = "Movie Bot: I'm sorry, I don't have information on that topic right now."

            except Exception as e:
                st.error(f"Error: {str(e)}")
                response = "Movie Bot: An error occurred. Please try again later."

            # Display response
            st.write(response)

def get_movie_name_from_context_or_query(user_input, keyword):
    match = re.search(rf'{keyword} (.+?)$', user_input.lower())
    if match:
        movie_name = match.group(1).strip()
        st.session_state.conversation_context['movie_info'] = movie_name
    elif 'movie_info' in st.session_state.conversation_context:
        movie_name = st.session_state.conversation_context['movie_info']
    else:
        movie_name = None
    return movie_name

if __name__ == '__main__':
    main()
