from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class login_facebook():
    def Test(self):
        baseUrl = "https://www.facebook.com/"
        driver = webdriver.Chrome()              #this line will open facebook in chrome
        driver.maximize_window()                 # for maximize the window
        driver.get(baseUrl)
        time.sleep(4)                                      #for pause
        username = driver.find_element(By.ID,"email")       #element find
        username.send_keys("abc@gmail.com")                 #for type in the box
        time.sleep(4)
        password = driver.find_element(By.ID,"pass")
        password.send_keys("abxcd")
        time.sleep(4)
        login_button = driver.find_element(By.NAME,"login")
        login_button.click()                                  #for click the button
        time.sleep(4)
a = login_facebook()
a.Test()