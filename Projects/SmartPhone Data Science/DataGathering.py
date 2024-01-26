import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



s = Service("C:/Users/vinay/Desktop/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://www.smartprix.com/mobiles')

#excluding out of stock and upcoming
driver.find_element(by=By.XPATH , value = '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(by = By.XPATH , value = '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/span').click()
time.sleep(1)

# clicking on load more
old_height = driver.execute_script('return document.body.scrollHeight')

while True:

    driver.find_element(by = By.XPATH , value = '/html/body/div[1]/main/div[1]/div[2]/div[3]').click()
    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(old_height)
    print(new_height)
    if old_height == new_height:
        break
    old_height = new_height

html = driver.page_source

with open('smartprix.html' , 'w' , encoding= 'utf-8') as f:
    f.write(html)
