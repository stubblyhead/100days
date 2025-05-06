from selenium import webdriver
from selenium.webdriver.common.by import By
import time

cycle_length = 15   
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


drv = webdriver.Chrome(options=chrome_options)
drv.get('https://orteil.dashnet.org/cookieclicker/')
time.sleep(5)
try:
    lang = drv.find_element(By.ID, 'langSelect-EN')
    lang.click()
except Exception:
    pass
time.sleep(5)
big_timeout = time.time() + 300
big_cookie = drv.find_element(By.ID, 'bigCookie')


while time.time() < big_timeout:
    short_timeout = time.time() + cycle_length
    while time.time() < short_timeout:
        big_cookie.click()
    # cookie_count = int(drv.find_element(By.ID, 'cookies').text.split()[0])
    try:
        upgrades = drv.find_element(By.ID, 'upgrades')
        upgrades = upgrades.find_elements(By.CLASS_NAME, 'enabled')
        upgrades.reverse()
    except Exception:
        pass
    for u in upgrades:
        try:
            u.click()
        except Exception:
            pass
    buildings = drv.find_element(By.ID, 'products')
    buildings = drv.find_elements(By.CLASS_NAME,'unlocked')
    building_list = []
    for i in range(len(buildings)):
        # cur_building = buildings[i].find_element(By.ID, f'productName{i}')
        cur_price = int(buildings[i].find_element(By.ID, f'productPrice{i}').text.replace(',','_'))

        building_list.append([cur_price, buildings[i]])
    building_list.sort()
    building_list.reverse()
    for b in building_list:
        b[1].click()
    
try:
    cps = drv.find_element(By.ID, 'cookiesPerSecond').text
except Exception:
    cps = drv.find_element(By.ID, 'cookiesPerSecond').text
print(f'\n\n{cycle_length} sec cycles\n{cps.split(': ')[1]} cookies/second')

    # focus on buildings for now, upgrade prices are kind of obscured
    # upgrades = drv.find_elements(By.ID, 'upgrades')
    # upgrades = drv.find_elements(By.CLASS_NAME, 'enabled')
    