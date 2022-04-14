import requests
import os

TMDB_API_KEY = os.environ['TMDBAPI']

# Get a Movie
# answer = requests.get(f"https://api.themoviedb.org/3/movie/500?api_key={TMDB_API_KEY}")
# print(answer.json())


def search_movie(search_query):
    search_query.replace(" ", "-")
    search = requests.get(f"https://api.themoviedb.org/3/search/movie?"
                          f"api_key={TMDB_API_KEY}&query={search_query}&"
                          f"language=en-US&page=1&include_adult=false")
    movies = search.json()['results']
    return movies


movie_data = search_movie(input("Insira o filme que você deseja procurar:\n"))

for movie in movie_data:
    print(movie["title"])
    print(movie["overview"])
