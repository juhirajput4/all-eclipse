
#We can find the value of any attribute

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FindElements():
    def test(self):
        driver = webdriver.Chrome()
        driver.get("https://letskodeit.teachable.com/courses")
        driver.maximize_window()
        # element1 = driver.find_element(By.ID, "search-courses")
        # time.sleep(2)
        # element1.send_keys("Javascript")

        myXpath = "//div[contains(text(),'Selenium WebDriver Bundle (Java + Python)')]"
        course = driver.find_element(By.XPATH, myXpath)
        print(course.text)



        name = 'Complete Test Automation Bundle'
        myXpath = "//div[contains(text(),'{0}')]"
        dynamicXpath = myXpath.format(name)
        course = driver.find_element(By.XPATH, dynamicXpath)
        print(course.text)

a = FindElements()
a.test()