import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



s = Service("C:/Users/vinay/Desktop/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('http://google.com')


# fetch the search input box using xpath
user_input = driver.find_element(by = By.XPATH , value = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/div/textarea')
user_input.send_keys('Campusx')  #-> passing campusx to search box
time.sleep(1)

user_input.send_keys(Keys.ENTER) #-> Entering the search

time.sleep(1)
# finding the website element
website = driver.find_element(by = By.XPATH , value = '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')
# opening campusx website.
website.click()

link2 = driver.find_element(by = By.XPATH , value = '//*[@id="1668425005116"]/span[2]/a')
link2.click()


