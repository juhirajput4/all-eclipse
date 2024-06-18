from GenericMethod.handy_wrappers import HandyWrapper
from GenericMethod.handy_wrappers import getBrowserDriver
from explicitWaitType import ExplicitWaitType

class UsingExplicitWaitType():
    def test(self):
        driver = getBrowserDriver('edge')
        # driver.execute_script("window.location = 'https://letskodeit.teachable.com'")
        driver.get("https://letskodeit.teachable.com")
        driver.maximize_window()
        # create object of handy wrapper, pass webdriver to constructor
        ewt = ExplicitWaitType(driver)

        element= ewt.waitForElement("//div[@id='navbar']//a[@href='/sign_in']", "xpath")
        if element is not None:
            element.click()

            email = ewt.waitForElement("email", "id")
            email.send_keys("test@gmail.com")





uW = UsingExplicitWaitType()
uW.test()

