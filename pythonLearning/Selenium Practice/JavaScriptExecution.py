from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JavaScriptExecution():
    def Test(self):
        baseUrl = "https://www.facebook.com/"
        driver = webdriver.Edge()           #this line will open facebook in chrome
        driver.maximize_window()                 # for maximize the window
        driver.execute_script("window.location = 'https://www.facebook.com/'")
        time.sleep(4)                                      #for pause
        # username = driver.find_element(By.ID,"email")       #element find
        username = driver.execute_script("return document.getElementById('email')")
        # in javascript function we don't have getElementsById, we only have getElementById and getElementByClass function
        username.send_keys("abc@gmail.com")                 #for type in the box
        time.sleep(4)

a = JavaScriptExecution()
a.Test()
