# pyTest - Selenium - Allure Hello World Script
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

import allure
import pytest

def test_allure_example():
    with allure.step("Allure step example"):
        pass

        