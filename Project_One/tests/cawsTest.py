from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class playWright():
    def test(self):
        baseUrl = "https://www.google.com/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        search_box = driver.find_element()