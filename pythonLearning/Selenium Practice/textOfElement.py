#we can print the text of any element

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FindElements():
    def test(self):
        driver = webdriver.Chrome()
        driver.get("https://www.marutisuzuki.com/corporate/careers/training-academy")
        driver.maximize_window()
        text1 = driver.find_element(By.XPATH, "//p[contains(text(),'Maruti Suzuki India Limited has been a pioneer in the automotive industry and being an industry leader in the passenger car segment it')]")
        print(text1.text)
        text2 = driver.find_element(By.PARTIAL_LINK_TEXT,"contact@maruti.co").text
        print(text2)


a = FindElements()
a.test()