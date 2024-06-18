from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_driver import seleniumDriver

class filter_PageClass(seleniumDriver):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    _filter = "//div[@class='scroll-child']/div[2]/div[2]/button[1]"

    def getFilter(self):
        self.clickElement(self._filter, By.XPATH)


    def apllyFilter(self):
        self.getFilter()