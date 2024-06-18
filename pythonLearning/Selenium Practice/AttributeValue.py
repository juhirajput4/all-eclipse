#We can find the value of any attribute

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FindElements():
    def test(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        element = driver.find_element(By.XPATH, "//a[@data-trackvalue='YFB Chosen']")
        print(element.get_attribute('data-trackaction'))



a = FindElements()
a.test()