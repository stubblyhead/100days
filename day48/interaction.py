from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


drv = webdriver.Chrome(options=chrome_options)
drv.get('https://en.wikipedia.org/wiki/Main_Page')
article_div = drv.find_element(By.ID, 'articlecount')
article_count = article_div.find_elements(By.CSS_SELECTOR, 'li a')[1].text
print(article_count)