"""
file name should start with test
test method name should start with test

py.test test_mod.py   # run tests in module
py.test somepath      # run all tests below somepath
py.test test_module.py::test_method  # only run test_method in test_module

-s to print statements
-v verbose
"""

import pytest

# 1. Without using fixture method
def test_methodA():
    print("Running method A")

def test_methodB():
    print("running method B")

# 2. With using fixture method
@pytest.fixture()
def setUp():
    print("once before every method")

def test_methodC():
    print("Running method C")

def test_methodD(setUp):
    print("running method D")