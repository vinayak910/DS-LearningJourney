import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



s = Service("C:/Users/vinay/Desktop/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://www.ajio.com/s/table-napkins-4720-51871')
time.sleep(2)
old_height = driver.execute_script('return document.body.scrollHeight') # height till the end of that page
counter = 0
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)') # scroll down till end of hght
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')
    time.sleep(2)
    print(new_height)
    print(old_height)
    counter+=1
    print(counter)
    if new_height == old_height:
        break
    old_height = new_height

html = driver.page_source

with open('ajio.html' , 'w' , encoding= 'utf-8') as f:
    f.write(html)