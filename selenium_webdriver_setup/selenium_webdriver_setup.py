# Selenium Hello World Script
#
# Setup:
#
# Download chrome driver from location:
# https://chromedriver.chromium.org/downloads
#
# Copy chromedriver file to location that is in PATH variable
# (It can be in Scripts/bin forlder of virtual environment)
#
# Start example django application to be tested:
# https://github.com/hooppler/DjangoQuickStart
#
# Copy chromedriver.exe to path C:\chromedriver

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
