# pyTest - Selenium Hello World Script
#
# 
# - File width test must have prefix 'test_' in its name.
# - Test method within file with tests must have prefih 'test_'.
#
# Only methods with test_ prefix consideres as tests.
# Other methods can be used as helper methods and test runer
# will not consider them as tests.
#
# Pytest has testruner script 'pytest'.
#
# Run tests:
# cd to directory that contain scripts and type from comand line:
# > pytest

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestClass:
    def test_check_helloworld_link(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')
        element = driver.find_element(By.LINK_TEXT, 'Helloworld!!!')
        element.click()

        