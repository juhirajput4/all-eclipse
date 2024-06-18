
# check this link for different types of order function - https://pytest-ordering.readthedocs.io/en/develop/
# cmd - pip install pytest-ordering
import pytest

@pytest.mark.run(order = 2)
def test_methodB():
    print("running test method B")

@pytest.mark.run(order = 3)
def test_methodC():
    print("Running test method C")

@pytest.mark.run(order = 8)
def test_methodD():
    print("running test method D")

@pytest.mark.run(order = 5)
def test_methodE():
    print("Running test method E")

@pytest.mark.run(order = 10)
def test_methodF():
    print("running test method F")
@pytest.mark.run(order = 1)
def test_methodA():
    print("Running test method A")

