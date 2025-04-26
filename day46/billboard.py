from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

with open('totallynotpasswords.txt') as f:
    SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET = f.read().strip().split(':')
SPOTIPY_REDIRECT_URI = 'https://example.com'

os.environ['SPOTIPY_CLIENT_ID'] = SPOTIPY_CLIENT_ID
os.environ['SPOTIPY_CLIENT_SECRET'] = SPOTIPY_CLIENT_SECRET
os.environ['SPOTIPY_REDIRECT_URI'] = SPOTIPY_REDIRECT_URI

date = input('What day to go back to? (YYYY-MM-DD) ? ')
# date = '2000-01-01'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/',headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')
chart = soup.find_all(name='div', class_='o-chart-results-list-row-container')

songs = []
for c in chart:
    track = c.find(name='h3', id='title-of-a-story').get_text().strip()
    artist = c.select('li ul li span')[0].get_text().strip()
    songs.append([track,artist])


scope = 'playlist-modify-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user = sp.current_user()['id']
sp_tracks = []
for s in songs:
    short_title = s[0].split('/')[0] # choose first track from a double-A side single
    short_title = short_title.split('(')[0] # sometimes chart includes parentheticals not included in spotify titles
    short_artist = s[1].split()[0] # first word of artist name is usually enough to nail down the right track
    trackresults = sp.search(q=f'track:{short_title} artist:{short_artist}',type='track')
    try:
        sp_tracks.append(trackresults['tracks']['items'][0]['uri'])
    except IndexError:
        print(f'Cant find "{s[0]}" by {s[1]}, should be at position {songs.index(s)}')

new_playlist = sp.user_playlist_create(user=user,name=f'Billboard Hot 100 for {date}',public=False)


sp.playlist_add_items(playlist_id=new_playlist['id'], items=sp_tracks)

print(new_playlist['external_urls']['spotify'])