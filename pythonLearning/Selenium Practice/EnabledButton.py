#We can whether button are enabled or not

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class EnabledButton():
    def test(self):
        driver = webdriver.Chrome()
        driver.get("https://training.openspan.com/login")
        driver.maximize_window()

        loginButtonElement = driver.find_element(By.ID,"login_button")
        isElementEnabled = loginButtonElement.is_enabled()
        print("login button is enabled "+ str(isElementEnabled))
        time.sleep(2)

        #enter the username and password and then check login button is enabled or not

        usernameElement = driver.find_element(By.ID,"user_name")
        usernameElement.send_keys("abc@gmail.com")
        passwordElement = driver.find_element(By.ID,'user_pass')
        passwordElement.send_keys('abc2345')

        #now check again for login button if its enabled or disabled
        isElementEnabled = loginButtonElement.is_enabled()
        print("login button is enabled " + str(isElementEnabled))

a = EnabledButton()
a.test()