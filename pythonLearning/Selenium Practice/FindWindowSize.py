from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FindWindowSize():
    def Test(self):
        baseUrl = "https://www.apexhours.com/salesforce-admin-training-free/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        # 1. By using Javascript function
        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("height:" + str(height))
        print("width:" + str(width))

        outerHeight = driver.execute_script("return window.outerHeight;")
        outerWidth = driver.execute_script("return window.outerWidth;")
        print("outerHeight:" + str(outerHeight))
        print("outerWidth:" + str(outerWidth))


        # 2. By using webdriver function
        size = driver.get_window_size()
        print(size.get('height'))
        print(size.get('width'))

        # if we want both height and width
        print(size)







a = FindWindowSize()
a.Test()