from selenium import webdriver
from selenium.webdriver.common.by import By

drv = webdriver.Chrome()
drv.get('https://www.amazon.com/dp/B075CYMYK6')

price_whole = drv.find_element(By.CLASS_NAME, 'a-price-whole')
price_fraction = drv.find_element(By.CLASS_NAME, 'a-price-fraction')

print(f'${price_whole}.{price_fraction}')