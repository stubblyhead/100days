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

# date = input('What day to go back to? (YYYY-MM-DD) ? ')
date = '2020-01-01'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/',headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')
chart = soup.find_all(name='div', class_='o-chart-results-list-row-container')

songs = []
for c in chart:
    songs.append(c.find(name='h3', id='title-of-a-story').get_text().strip())

scope = 'user-library-read'
lz_id = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

