from bs4 import BeautifulSoup
import requests

endpoint_url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(endpoint_url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all(name='h3', class_='title')

title_list = []

for t in titles:
    title_list.append(t.text)

title_list = title_list[::-1]

with open('movie_list.txt', 'w') as f:
    for t in title_list:
        f.write(t + '\n')


