# pyTest Group Tests In Classes
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
# (venv) C:\<path>\Python\pytest_selenium_quickstart\pytest_group_in_classes>pytest
# ================================== test session starts ==================================
# platform win32 -- Python 3.8.6, pytest-7.1.2, pluggy-1.0.0
# rootdir: C:\<path>\pytest_selenium_quickstart\pytest_group_in_classes
# collected 3 items
# 
# test_gourp_in_classes.py .F.                                                       [100%]
# 
# ======================================= FAILURES ========================================
# ___________________________________ TestClass.test_2 ____________________________________
# 
# self = <test_gourp_in_classes.TestClass object at 0x000002A1B090EA60>
# 
#     def test_2(self):
# >       assert 2 == 3
# E       assert 2 == 3
# 
# test_gourp_in_classes.py:36: AssertionError
# ================================ short test summary info ================================
# FAILED test_gourp_in_classes.py::TestClass::test_2 - assert 2 == 3
# ============================== 1 failed, 2 passed in 0.17s ==============================


class TestClass:
    def helper_function(self):
        return True
    
    def test_1(self):
        assert self.helper_function() == True
        
    def test_2(self):
        assert 2 == 3
        
    def test_3(self):
        assert True




