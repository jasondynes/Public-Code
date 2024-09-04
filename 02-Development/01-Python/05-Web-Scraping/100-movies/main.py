import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
top_100_films_web_Page = response.text

soup = BeautifulSoup(top_100_films_web_Page, "html.parser")

# film_title = soup.find(name="h3", class_="title")
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

# Note: changes encoding from UTF-8 to ISO to handle some characters found in web scrape data
with open("movies.txt", mode="w", encoding='iso-8859-1') as file:
    for movie in movies:
        file.write(f"{movie}\n")
