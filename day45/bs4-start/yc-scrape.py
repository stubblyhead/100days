from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

title_lines = soup.find_all(name='span', class_='titleline')

for line in title_lines:
    a_tag = line.find(name='a')
    print(a_tag.text)
    print(a_tag.get('href') + '\n')