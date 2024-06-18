from selenium import webdriver
from GenericMethod.handy_wrappers import HandyWrapper
from GenericMethod.handy_wrappers import getBrowserDriver
import time

class UsingWrapper():
    def test(self):
        baseurl = "https://courses.letskodeit.com/practice"
        #driver = webdriver.Chrome()
        driver = getBrowserDriver('edge')
        driver.get(baseurl)
        driver.maximize_window()
        # create object of handy wrapper, pass webdriver to constructor
        hw = HandyWrapper(driver)

        element= hw.getElement("opentabs", "id")
        if element is not None:
            element.click()


        enterName = hw.getElement('enter-name',"name")
        hw.enterInElement(enterName,'juhi rajput')
        time.sleep(4)

        # line 26 is using generic method to take screenshot
        hw.takeScreenshot()

    def test2(self):
        baseurl = "https://courses.letskodeit.com/practice"
        driver = getBrowserDriver('chROME')
        driver.get(baseurl)
        driver.maximize_window()
        # create object of handy wrapper, pass webdriver to constructor
        hw = HandyWrapper(driver)

        result = hw.isElementPresent("id", "opentab")
        print(result)

        result2 = hw.elementPresenceCheck("id", "opentabs")
        print(result2)
        result3 = hw.elementPresenceCheck("id", "search")
        print(result3)

uW = UsingWrapper()
uW.test()