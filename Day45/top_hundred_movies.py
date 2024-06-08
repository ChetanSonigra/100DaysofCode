from bs4 import BeautifulSoup
import requests

url = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
movies_page = BeautifulSoup(response.text,"html.parser")

movies = [x.getText() for x in movies_page.find_all(name="h3",class_="listicleItem_listicle-item__title__BfenH")]

# print(movies)

with open("Day45/movies.txt","w",encoding="utf-8") as f:
    movies.reverse()
    for x in movies:
        f.write(f"{x}\n")