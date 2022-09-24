# pyTest Hello World Script
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
#
# Result will be:
# ============================= test session starts =============================
# platform win32 -- Python 3.8.6, pytest-7.1.2, pluggy-1.0.0
# rootdir: F:\03 WorkSpace\Python\pytest_selenium_quickstart
# collected 1 item
#
# pytest_hello_world\test_hello_world.py .                                 [100%]
#
# ============================== 1 passed in 0.02s ==============================


def helper_function():
    return True


def test_hello_world():
    assert helper_function() == True