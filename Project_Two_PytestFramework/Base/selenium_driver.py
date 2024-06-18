from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.customLogger import CustomLogger
import logging
import time

import logging


class seleniumDriver():

    cl = CustomLogger(loggerName="selenium Driver", logLevel = logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower() # iD => id / ID => id / Id => id
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'class_name':
            return By.CLASS_NAME
        elif locatorType == 'link_text':
            return By.LINK_TEXT
        else :
            return False

    def getElement(self, locatorType, path):
        element = None
        try:
            self.driver.implicitly_wait(10)
            byType = self.getByType(locatorType)

            element = self.driver.find_element(byType,path)
            self.cl.info("Element found with locator: " + path +
                          " and  locatorType: " + locatorType)

        except:
            self.cl.error("Element not found with locator: " + path +
                          " and  locatorType: " + locatorType)
        return element
        time.sleep(2)

    def enterInElement(self,element, text):
        element.send_keys(text)

    def clickElement(self, path, locatorType):
        self.getElement(locatorType, path).click()

    def isElementPresent(self, locatorType, path):
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,path)
            if element is not None:
                print("element found")
                return True
            else:
                print("element not found")
                return False

        except:
            print("in exception element not found")
            return False

    def scrolling(self, path, locatorType):
        element = self.getElement(locatorType, path)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(4)

    def switchIframes(self, num):
        self.driver.switch_to.frame(num)
    def switchDefault(self):
        self.driver.switch_to.default_content()

