from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class basicTestOfMarutiSuzuki():
    def Test(self):
        driver = webdriver.Chrome()
        driver.get("https://www.marutisuzuki.com/corporate/careers/training-academy")
        driver.maximize_window()
        driver.fullscreen_window()
        time.sleep(4)
        print(driver.title)
        time.sleep(4)
        clickOnMarutiSuzuki = driver.find_element(By.LINK_TEXT,'HOME')
        clickOnMarutiSuzuki.click()
        print(driver.current_url)
        time.sleep(4)
        driver.back()
        time.sleep(4)
        driver.refresh()
        time.sleep(4)
        driver.forward()
        time.sleep(4)
        driver.minimize_window()
        time.sleep(4)

a = basicTestOfMarutiSuzuki()
a.Test()

