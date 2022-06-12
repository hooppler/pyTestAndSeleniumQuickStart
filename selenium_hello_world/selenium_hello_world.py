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
# Path of the chromedriver can be specified from the test:
# service = Service(r'C:\chromedriver\chromedriver.exe')
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options=options, service=service)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")

element = driver.find_element(By.LINK_TEXT, 'Helloworld!!!')

element.click()