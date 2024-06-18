import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Base.selenium_driver import seleniumDriver

class navigationPageClass(seleniumDriver):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    _home = "HOME"
    _all_courses = "(//a[@href='/courses'])[1]"
    _userIcon = "//span[@class='caret']"

    def navigateToHome(self):
        self.clickElement(self._home, By.LINK_TEXT)

    def navigateToAllCouses(self):
        self.clickElement(self._all_courses, By.XPATH)

    def navigateToUserIcon(self):
        self.clickElement(self._userIcon, By.XPATH)











