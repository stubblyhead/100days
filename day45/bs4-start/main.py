from bs4 import BeautifulSoup

with open('website.html') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)

a_tags = soup.find_all(name='a')
print(len(a_tags))



