from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class radioButton():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()

        radioElement = driver.find_element(By.ID,"bmwradio")
        radioElement.click()
        time.sleep(2)

        radioElements = driver.find_elements(By.XPATH,"//input[@type='radio']")
        for i in radioElements:
            if i.is_selected() is False:
                i.click()
                time.sleep(2)


a = radioButton()
a.test()