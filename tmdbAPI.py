# ---------------------------------- IMPORTS ----------------------------------
import requests
import os


# --------------------------------- CONSTANTS ---------------------------------
# API Key for request. Stored as an environment variable for security reasons.
TMDB_API_KEY = os.environ['TMDBAPI']


# --------------------------------- FUNCTIONS ---------------------------------
def search_movie(search_query):
    # This functions receives a string and returns a JSON with all the movies
    # with this string on its title.
    search_query.replace(" ", "-")
    search = requests.get(f"https://api.themoviedb.org/3/search/movie?"
                          f"api_key={TMDB_API_KEY}&query={search_query}&"
                          f"language=en-US&page=1&include_adult=false")
    movies = search.json()['results']
    return movies


# --------------------------------- TEST CODE ---------------------------------
# Test code belows uses an input to test the functions of this script.
if __name__ == "__main__":
    movie_data = search_movie(input("Insira o filme que você deseja procurar:\n"))

    for movie in movie_data:
        print(movie["title"])
        print(movie["overview"])
