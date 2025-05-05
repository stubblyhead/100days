from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


drv = webdriver.Chrome(options=chrome_options)
drv.get('https://www.python.org/')
events = drv.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
events = events.find_elements(By.TAG_NAME, 'li')
event_dict = {}
for i in range(len(events)):
    this_event = events[i]
    date = this_event.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0]
    name = this_event.find_element(By.TAG_NAME, 'a').text
    event_dict[i] = {'time': f'{date}', 'name': f'{name}'}


print(event_dict)