from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def getBrowserDriver(name):
    name = name.lower()
    if(name=='chrome'):
        return webdriver.Chrome()
    if(name=='edge'):
        return webdriver.Edge()
    return webdriver.Chrome()

class HandyWrapper():

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
        else :
            return False

    def getElement(self,path, locatorType):
        element = None
        try:
            self.driver.implicitly_wait(10)
            byType = self.getByType(locatorType)

            element = self.driver.find_element(byType,path)
            print('Element Found')

        except:
            print('Element Not Found')
        return element
        time.sleep(2)


    def enterInElement(self,element, text):
        element.send_keys(text)

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

    def elementPresenceCheck(self, locatorType, path):
        byType = self.getByType(locatorType)
        elementList = self.driver.find_elements(byType, path)
        if len(elementList) > 0:
            print("element found")
            return True
        else:
            print("element not found")
            return False

    def takeScreenshot(self):
        fileDir = "C:\\Users\\Cloud Analogy\\Desktop\\"
        fileName = str(round(time.time() * 1000)) + ".png"
        finalName = fileDir + fileName

        try:
            self.driver.save_screenshot(finalName)
            print(finalName)
        except:
            print("location is not found")




