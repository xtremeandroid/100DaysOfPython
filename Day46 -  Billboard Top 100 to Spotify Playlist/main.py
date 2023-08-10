import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# pip install python-dotenv
from dotenv import load_dotenv
import os
load_dotenv()


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt",
        username=os.getenv("USERNAME"),
    )
)
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD : ")
top_100_music_list = []
song_uris = []
year = date.split("-")[0]

URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL)
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")
music_elements = soup.find_all("div", class_="o-chart-results-list-row-container")

for element in music_elements:
    music_name = element.find("h3").get_text()
    top_100_music_list.append(music_name.strip())

for song in top_100_music_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user_id, name=f"{date} Billboard Top 100", public=False, description="Top 100 "
                                                                                         "Hot Songs From Billboard")
sp.playlist_add_items(playlist["id"], song_uris)