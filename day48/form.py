from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


drv = webdriver.Chrome(options=chrome_options)
drv.get('https://secure-retreat-92358.herokuapp.com/')

fname = drv.find_element(By.NAME, 'fName')
fname.send_keys('Stubbs')
lname = drv.find_element(By.NAME, 'lName')
lname.send_keys('Head')
email = drv.find_element(By.NAME, 'email')
email.send_keys('27823133+stubblyhead@users.noreply.github.com')
button = drv.find_element(By.CLASS_NAME, 'btn')
button.click()