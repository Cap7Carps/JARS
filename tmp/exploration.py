import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


spotify_id = '2e28dde60bc145bdb29156971765acef'
spotify_secret = 'f11e07eecbde4976b59c63ca93dc0464'


# os.putenv('SPOTIPY_CLIENT_ID', spotify_id)
# os.putenv('SPOTIPY_CLIENT_SECRET', spotify_secret)

os.environ['SPOTIPY_CLIENT_ID'] = spotify_id
os.environ['SPOTIPY_CLIENT_SECRET'] = spotify_secret

l = os.getenv('SPOTIPY_CLIENT_ID')

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

aa = sp.artist('5AE52XrC6wM9wzhtSQDupS')

painful_album = sp.album('https://open.spotify.com/album/5OPn2TtypUotqcA7K5C0IE?si=-tf_CxfsRH-vfXomNUXpCg')

search_query = 'a'
search_type = 'artist'

search_result = sp.search(search_query, type=search_type, limit=30)

for result in search_result['artists']['items']:
    artist = sp.artist((result['id']))
    print(repr(artist))
