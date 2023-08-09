import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text
soup = BeautifulSoup(content, "html.parser")


movies_list = []
items = soup.find_all("div", class_="listicle-item")
for i,item in enumerate(items):
    movie_name = item.find('img').get("alt")
    movie_str = f"{100 - i}) {movie_name}.\n"
    movies_list.append(movie_str)

with open("movies_list.txt", "w") as datafile:
    for movie in movies_list:
        datafile.write(movie)
