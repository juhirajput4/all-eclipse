from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from handy_wrappers import HandyWrapper

class ExplicitWaitType():
    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrapper(driver)

    def waitForElement(self, path, locatorType):
        element = None
        try:
            # self.driver.implicitly_wait(10)
            locatorByType = self.hw.getByType(locatorType)
            wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
            element = wait.until(EC.visibility_of_element_located((locatorByType , path)))
            print("element found")

        except:
            print('Element Not Found')
        return element

