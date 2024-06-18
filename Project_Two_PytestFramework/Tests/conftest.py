import pytest
from selenium import webdriver
from Base.WebDriverFactory import WebdriverFactory
from  Pages.LoginClass.loginPageClass import loginPageClass


@pytest.fixture(scope='class')
def setupDriver(request, browser):
    print("setup Driver")

    #  in third video
    wdf = WebdriverFactory(browser)
    driver = wdf.getWebdriverInstance()
    lp = loginPageClass(driver)
    lp.login("juhi.rajput@cloudanalogy.com", "abcabc")

    """
    baseURL = "https://courses.letskodeit.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseURL)
    """
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    print("tear down")
    driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')