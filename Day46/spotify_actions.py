import spotipy,os,requests
from spotipy.oauth2 import SpotifyOAuth

class Spotify:
    def __init__(self,user_date) -> None:
        self.user_date = user_date
        self.scope = "playlist-modify-private"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
                                               client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
                                               redirect_uri="http://localhost:8000/",
                                               scope=self.scope,
                                               show_dialog=True,
                                               cache_path=".cache"))
        self.get_user_id()
        self.get_track_uris()

    def get_user_id(self):
        self.user_id = self.sp.current_user()['id']
        
    def get_track_uris(self):
        with open("Day46/songs.txt") as f:
            songs = f.read()

        self.track_uris = []
        try:
            for song in songs.split("\n"):
                result = self.sp.search(q=f"track: {song.strip()}",type="track")
                # print(result)
                track_uri = result['tracks']['items'][0]['uri']
                self.track_uris.append(track_uri)
        except Exception as e:
            return e
        
    def create_playlist(self):
        result = self.sp.user_playlist_create(user=self.user_id,name=f"{self.user_date} Billboard 100",public=False)
        self.playlist_id = result['id']

    def add_songs_to_playlist(self):
        result = self.sp.playlist_add_items(self.playlist_id,self.track_uris)


