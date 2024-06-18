from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Attribute_valuse_element():
    def test(self):
        baseurl = "https://www.facebook.com/"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        password = driver.find_element(By.ID,"pass")
        x = password.get_attribute("type")
        print("value of the type attribute is:" + x)               #find the value of the attribute
        driver.close()

a = Attribute_valuse_element()
a.test()