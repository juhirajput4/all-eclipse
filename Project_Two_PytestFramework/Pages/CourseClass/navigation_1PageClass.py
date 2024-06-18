import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Base.selenium_driver import seleniumDriver
from selenium.webdriver.support.select import Select

class coursePageClass(seleniumDriver):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    _search_Course = "//input[@id='search']"
    _search = "//button[@type='submit']"
    _clickOnCourse = "(//div[@class='zen-course-list'])[1]"
    _enrollCourse = "//button[text()='Enroll in Course']"
    _cardNumber = "cardnumber"
    _expiryDate = "//input[@autocomplete='cc-exp']"
    _securityCode = "//input[@name='cvc']"
    _country = "country-list"
    _buyButton = "(//i[@class='fa fa-arrow-right'])[1]"
    _paymentInformation = "//h3[text()='Payment Information ']"

    def getSearchCourse(self):
        return self.getElement(By.XPATH, self._search_Course)
    def getCardNumber(self):
        return self.getElement(By.NAME, self._cardNumber)
    def getExpireDate(self):
        return self.getElement(By.XPATH, self._expiryDate)
    def getSecurityCode(self):
        return self.getElement(By.XPATH, self._securityCode)

    def enterCourseName(self, courseName):
        self.enterInElement(self.getSearchCourse(), courseName)

    def getSearch(self):
        self.clickElement(self._search, By.XPATH)

    def getCourse(self):
        self.clickElement(self._clickOnCourse, By.XPATH)

    def getEnrollCourse(self):
        self.clickElement(self._enrollCourse, By.XPATH)

    def getScrollDown(self):
        self.scrolling(self._paymentInformation, By.XPATH)

    def enterCardNumber(self, cardNumber):
        self.switchIframes(0)
        self.enterInElement(self.getCardNumber(), cardNumber)
        self.switchDefault()

    def enterExpireDate(self, exDate):
        self.switchIframes(1)

        self.enterInElement(self.getExpireDate(), exDate)
        self.switchDefault()

    def enterSecurityCode(self, securityCode):
        self.switchIframes(2)
        self.enterInElement(self.getSecurityCode(), securityCode)
        self.switchDefault()

    def getCountryOptions(self):
        element = self.getElement(By.NAME, self._country)
        sel = Select(element)
        return sel

    def clickBuy(self):
        self.clickElement(self._buyButton, By.XPATH)

    def presentElement(self):
        self.isElementPresent(By.XPATH, "//li[@class='card-no cvc expiry text-danger']/span")
        print("element is present")


    def course(self, courseName, cardNumber, exDate, securityCode, ele):
        self.enterCourseName(courseName)
        time.sleep(3)
        self.getSearch()
        time.sleep(3)
        self.getCourse()
        self.getEnrollCourse()
        time.sleep(3)
        self.getScrollDown()
        time.sleep(3)
        # self.switchIframes()
        self.enterCardNumber(cardNumber)
        time.sleep(3)
        # self.switchDefault()
        print("card number")
        # self.switchIframes()
        self.enterExpireDate(exDate)
        time.sleep(3)
        # self.switchDefault()
        # self.switchIframes()
        self.enterSecurityCode(securityCode)
        time.sleep(3)
        # self.switchDefault()
        countryOptions = self.getCountryOptions()
        countryOptions.select_by_visible_text(ele)
        self.clickBuy()
        # self.presentElement()
        time.sleep(3)



