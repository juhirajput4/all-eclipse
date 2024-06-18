from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class usefullMethods():
    def getText(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()

        openTabElement= driver.find_element(By.ID,"opentab")
        elementText = openTabElement.text
        print(elementText)


    def getAttribute(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()

        enterName = driver.find_element(By.XPATH,"//input[@name='enter-name']")
        elementValue = enterName.get_attribute("placeholder")
        print(elementValue)

a = usefullMethods()
a.getAttribute()