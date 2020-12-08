import secrets
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class get_play_history:

    def __init__(self):
        self.token = secrets.spotify_token
        self.user_id = secrets.user_id
        self.spotify_id = secrets.SPOTIFY_ID
        self.spotify_secret = secrets.SPOTIFY_SECRET
        self.redirect = secrets.redirect
        self.spotify_headers = {"Content-Type": "application/json",
                                "Authorization": f"Bearer {self.token}"}
        self.playlist_id = ''
        self.scope = "user-read-recently-played"

    def get_recently_played(self):
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(self.spotify_id, self.spotify_secret, self.redirect, scope=self.scope,
                                      cache_path='NONE'))
        recently_played_tracks = sp.current_user_recently_played(limit=1)
        # recent_songs = []
        # for idx, item in enumerate(recently_played_tracks['items']):
        #     track = item['track']
        #     name = track['name']
        #     recent_songs.append(name)
        #
        # recent_songs = list(dict.fromkeys(recent_songs))
        # print(recent_songs)

        # recent_artists = []
        # for idx, item in enumerate(recent_songs):
        #     track = item['track']
        #     artist = track['album']['artists'][0]['name']
        #     recent_artists.append(artist)
        #
        # print(recent_artists)

        song_info = dict()
        for idx, item in enumerate(recently_played_tracks['items']):
            track = item['track']
            song = track['name']
            artist = track['album']['artists'][0]['name']
            print (f"{song} by {artist}" )
            song_info[song] = artist


        # for idx, item in enumerate(most_recent):
        #     track = item['track']
        #     artist = track['album']['artists'][0]['name']
        #     most_recent.append(artist)

        return song_info


if __name__ == '__main__':
    songs = get_play_history()
    songs.get_recently_played()
