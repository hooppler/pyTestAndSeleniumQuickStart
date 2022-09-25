# Selenium Hello World Script
#
# Setup:
#
# Download chrome driver from location:
# https://chromedriver.chromium.org/downloads
#
# Copy chromedriver.exe to path C:\chromedriver
#
# This application is using www.google.com as example

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(r'C:\chromedriver\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options, service=service)

driver.get('https://www.google.com')

element = driver.find_element(By.NAME, 'q')

element.send_keys('Test')
element.send_keys(Keys.ENTER)

driver.close()
