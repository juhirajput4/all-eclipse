from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

class Checkbox():

    def test(self):
        baseurl = "https://biotheranostics--lisqa.sandbox.my.site.com/s/login/?ec=302&startURL=%2Fs%2F"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        time.sleep(3)
        driver.implicitly_wait(10)
        username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        username.send_keys("test")
        time.sleep(4)

a = Checkbox()
a.test()