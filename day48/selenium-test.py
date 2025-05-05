from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


drv = webdriver.Chrome(options=chrome_options)
drv.get('https://www.amazon.com/dp/B075CYMYK6?th=1')
captcha = drv.find_element(By.LINK_TEXT, "Try different image")
captcha.click()

price_whole = drv.find_element(By.CLASS_NAME, 'a-price-whole')
price_fraction = drv.find_element(By.CLASS_NAME, 'a-price-fraction')

print(f'${price_whole.text}.{price_fraction.text}')