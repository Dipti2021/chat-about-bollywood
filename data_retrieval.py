# data_retrieval.py

import requests

def search_movie(movie_name):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": movie_name,
        "format": "json"
    }
    response = requests.get(url, params=params)
    return response.json()

def get_movie_summary(title):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    response = requests.get(url)
    return response.json()

def get_movie_info(movie_name):
    search_results = search_movie(movie_name)
    if search_results['query']['search']:
        top_result_title = search_results['query']['search'][0]['title']
        movie_summary = get_movie_summary(top_result_title)
        return movie_summary
    else:
        return None
