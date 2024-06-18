from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Signup_facebook():
    def Test(self):
        baseUrl = "https://www.facebook.com/login/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        time.sleep(4)
        username = driver.find_element(By.CLASS_NAME,"_97w5")
        username.click()

a = Signup_facebook()
a.Test()