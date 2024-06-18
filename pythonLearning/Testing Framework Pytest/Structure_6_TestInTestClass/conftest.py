#  pytest -v -s test_5_CommandLineArg.py --browser chrome
import pytest

@pytest.fixture(scope="class")
def moduleSetUp(request, browser):

    if browser == "Chrome":
        value = 10
        print("test running in chrome browser")
    else:
        value = 20
        print("test running in edge browser")
    if request.cls is not None:
        request.cls.num = value
    yield value
    print("module end")

# this method is provided by pytest module so we always put same name of the method.
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")





