import requests
from bs4 import BeautifulSoup

class BillBoard:
    def __init__(self,user_date) -> None:
        self.url = f"https://www.billboard.com/charts/hot-100/{user_date}/"
        self.soup = BeautifulSoup(requests.get(self.url).text, "html.parser")
        self.song_titles = [x.string.strip() for x in self.soup.select(selector="li h3[id=title-of-a-story]")]
        # print(song_titles,len(song_titles))

    def write_top_songs(self):
        with open("Day46/songs.txt","w") as f:
            f.write("\n".join(self.song_titles))

