#Here I have locate multiple elements

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FindElements():
    def test(self):
        driver = webdriver.Chrome()
        driver.get("https://www.marutisuzuki.com/corporate/careers/training-academy")
        driver.maximize_window()
        lista = driver.find_elements(By.TAG_NAME,"a")
        print(len(lista))
        for i in lista:
            print(i.text)
            # print(i)


a = FindElements()
a.test()
