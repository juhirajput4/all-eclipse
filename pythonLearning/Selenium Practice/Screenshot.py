from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshot():
    def test(self):
        baseUrl = "https://www.facebook.com/"
        location = "/home/ca/Desktop/Screenshot/screenshots.png"
        driver = webdriver.Chrome()  # this line will open facebook in chrome
        driver.maximize_window()  # for maximize the window
        driver.get(baseUrl)
        time.sleep(4)  # for pause
        username = driver.find_element(By.ID, "email")  # element find
        username.send_keys("abc@gmail.com")  # for type in the box
        time.sleep(4)
        try:
            driver.save_screenshot(location)
        except:
            print("location not found")

        password = driver.find_element(By.ID, "pass")
        password.send_keys("abxcd")
        time.sleep(4)

        login_button = driver.find_element(By.NAME, "login")
        login_button.click()  # for click the button
        time.sleep(4)

        # for same location and file name same as previous screenshot it will override
        try:
            driver.save_screenshot(location)
        except:
            print("location not found")

    def test1(self):
        baseUrl = "https://www.facebook.com/"
        location = "/home/ca/Desktop/Screenshot/screenshotss.png"
        driver = webdriver.Chrome()  # this line will open facebook in chrome
        driver.maximize_window()  # for maximize the window
        driver.get(baseUrl)
        time.sleep(4)  # for pause
        username = driver.find_element(By.ID, "email")  # element find
        username.send_keys("abc@gmail.com")  # for type in the box
        time.sleep(4)

        # we need to pass driver to function because to get current instance of browser. Like which url is open, which field have what value
        self.takeScreenshot(driver)

        password = driver.find_element(By.ID, "pass")
        password.send_keys("abxcd")
        time.sleep(4)

        self.takeScreenshot(driver)

        login_button = driver.find_element(By.NAME, "login")
        login_button.click()  # for click the button
        time.sleep(4)


    def takeScreenshot(self, driver):

        fileDir = "/home/ca/Desktop/Screenshot/screenshotss.png"
        fileName = str(round(time.time() * 1000)) + ".png"


        finalName = fileDir + fileName
        try:
            driver.save_screenshot(finalName)
            print(finalName)
        except:
            print("location not found")


a = Screenshot()
a.test1()