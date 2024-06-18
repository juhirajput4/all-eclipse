import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Base.selenium_driver import seleniumDriver
from Pages.LoginClass.navigationPageClass import navigationPageClass

class loginPageClass(seleniumDriver):

    def __init__(self, driver):
        self.driver = driver
        self.nav = navigationPageClass(driver)
        super().__init__(driver)

    _signIn_link = "//a[@href='/login']"
    _username_field = "(//input[@id='email'])[1]"
    _password_field = "//input[@id='password']"
    _login_button = "//button[@id='login']"
    _all_courses = "(//a[@href='/courses'])[1]"
    _search_Course = "//input[@id='search']"
    _logout_button = "//a[@href='/logout']"

    # def getSignInLink(self):
    #     return self.getElement(By.XPATH, self._signIn_link)

    def getUsernameField(self):
        return self.getElement(By.XPATH, self._username_field)

    def getPasswordField(self):
        return self.getElement(By.XPATH, self._password_field)

    # def getLoginField(self):
    #     return self.getElement(By.XPATH, self._login_button)

    # def getallCoursesField(self):
    #     return self.getElement(By.LINK_TEXT, self._all_courses)

    def clickSignInLink(self):
        self.clickElement(self._signIn_link, By.XPATH)

    def enterUsernameField(self, username):
        self.enterInElement(self.getUsernameField(), username)

    def enterPasswordField(self, password):
        self.enterInElement(self.getPasswordField(), password)

    def clickLoginButton(self):
        self.clickElement(self._login_button, By.XPATH)

    def login(self, username, password):
        self.clickSignInLink()
        self.enterUsernameField(username)
        self.enterPasswordField(password)
        self.clickLoginButton()
        time.sleep(3)

    def logout(self):
        self.nav.navigateToUserIcon()
        time.sleep(3)
        self.clickElement(self._logout_button, By.XPATH)




