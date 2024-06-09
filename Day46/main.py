from bs4 import BeautifulSoup
import requests
from dateutil import parser
from spotify_actions import Spotify
from billboard import BillBoard

user_input = input('Which year do you want to travel to? Type data in this format: YYYY-MM-DD: ')

try:
    user_date = parser.parse(user_input)
except Exception:
    print("Provide valid date")

user_date = user_date.strftime("%Y-%m-%d")
# print(user_date)

bill_board =  BillBoard(user_date)

bill_board.write_top_songs()

spotify = Spotify(user_date)

spotify.create_playlist()

spotify.add_songs_to_playlist()