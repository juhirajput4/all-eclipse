#  pytest -v -s test_5_CommandLineArg.py --browser chrome --html=htmlReport.html
import pytest


@pytest.yield_fixture(scope="module")
def setUp(operatingSystem):
    print("Running Conftest once before every method", operatingSystem)
    yield
    print("Running Conftest once after every method")


@pytest.yield_fixture()
def moduleSetUp(browser, operatingSystem):
    if browser == "Chrome":
        print("test running in chrome browser")
    else:
        print("test running in edge browser")
    print("module setup P", browser, operatingSystem)
    yield
    print("module end")

# this method is provided by pytest module so we always put same name of the method.
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--operatingSystem", help="enter os")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def operatingSystem(request):
    return request.config.getoption("--operatingSystem")

