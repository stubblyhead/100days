from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

title_lines = soup.find_all(name='tr', class_='athing submission')
max_score = [0, '', '']

for line in title_lines:
    span = line.select('span a')
    article_id = line.get('id')
    a_tag = span[0]
    article_title = a_tag.text
    article_url = a_tag.get('href')
    score_line = soup.find(name='span', id=f'score_{article_id}')
    score = int(score_line.text.split()[0])
    if score > max_score[0]:
        max_score = [score, article_title, article_url]

print(max_score)
