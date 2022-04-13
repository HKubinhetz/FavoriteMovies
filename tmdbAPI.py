import requests
import os

TMDB_API_KEY = os.environ['TMDBAPI']

answer = requests.get(f"https://api.themoviedb.org/3/movie/550?api_key={TMDB_API_KEY}")
print(answer.json())

# TO DO!
# https://www.udemy.com/course/100-days-of-code/learn/lecture/22616320#questions/16005400
#
# You will need to read the documentation on The Movie Database to figure out how to request
# for movie data by making a search query.
#
# https://developers.themoviedb.org/3/search/search-movies
#
# HINT 1: The "Try it out" tab on the API docs is particularly useful to see the structure of
# the request and the data you can expect to get back.
#
# HINT 2: We covered how to make API requests a long time ago on Day 33, it might be worth
# reviewing the knowledge there if you get stuck.
#
# Using the data you get back from the API, you should render the select.html page and add all the
# movie title and year of release on to the page. This way, the user can choose the movie they want to add.
# There are usually quite a few movies under similar names.

