# data_retrieval.py

from imdb import IMDb
import requests

# Initialize IMDb access
ia = IMDb()

# Function to search for a movie and retrieve its details
def search_movie(movie_name):
    # Use IMDbPY to search for the movie
    movies = ia.search_movie(movie_name)
    return movies

# Function to get movie summary from Wikipedia
def get_movie_summary(title):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    response = requests.get(url)
    return response.json()

# Function to get release year of a movie
def get_release_year(movie_name):
    movies = search_movie(movie_name)
    if movies:
        movie_id = movies[0].movieID
        movie = ia.get_movie(movie_id)
        return movie.get('year')
    else:
        return None

# Function to get list of actors in a movie
def get_actors(movie_name):
    movies = search_movie(movie_name)
    if movies:
        movie_id = movies[0].movieID
        movie = ia.get_movie(movie_id)
        return [actor['name'] for actor in movie.get('cast')]
    else:
        return None

# Function to get director of a movie
def get_director(movie_name):
    movies = search_movie(movie_name)
    if movies:
        movie_id = movies[0].movieID
        movie = ia.get_movie(movie_id)
        return movie.get('director')[0]['name']
    else:
        return None

# Function to get awards of a movie (dummy function for demonstration)
def get_awards(movie_name):
    movies = ia.search_movie(movie_name)
    
    if movies:
        movie_id = movies[0].movieID
        movie = ia.get_movie(movie_id)
        
        awards = movie.get('awards')
        if awards:
            return awards
        else:
            return "No awards information available."
    else:
        return "No movie found."

# Function to get movie information
def get_movie_info(movie_name):
    summary = get_movie_summary(movie_name)
    if summary:
        return summary['extract']
    else:
        return None
