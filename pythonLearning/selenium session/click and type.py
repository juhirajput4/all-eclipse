from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndType():

    def test(self):
       driver = webdriver.Edge()
       baseUrl = "https://www.facebook.com/"
       driver.maximize_window()
       driver.get(baseUrl)
       time.sleep(2)

       # Entering the user name
       username = driver.find_element(By.ID,"email")
       username.send_keys("abc@facebook.com")

       #Entering the pass
       pas = driver.find_element(By.ID,"pass")
       pas.send_keys("134567")
       time.sleep(2)

       #clicking on the login button
       login = driver.find_element(By.NAME,"login")
       login.click()
       time.sleep(4)
       driver.close()


a = ClickAndType()
a.test()



