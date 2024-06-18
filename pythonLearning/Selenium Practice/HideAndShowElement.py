#We can find the value of any attribute

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FindElements():
    def test(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        driver.maximize_window()
        element1 = driver.find_element(By.ID, "myDIV").is_displayed()
        print("element displayed: " + str(element1))
        time.sleep(2)

        driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
        element2 = driver.find_element(By.ID, "myDIV").is_displayed()
        print("element are not displayed: " + str(element2))


    def test1(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/hotels")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//span[@class='txt-ellipses hotel_passengerBox travellerPaxBox']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//span[@class='ddSpinnerPlus'])[2]").click()
        time.sleep(2)
        ele = driver.find_element(By.XPATH, "//div[@class='agedropdown']").is_displayed()
        print("element displayed: " + str(ele))

    def test2(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/hotels")
        driver.maximize_window()
        try:
            ele = driver.find_element(By.XPATH, "//div[@class='agedropdown']").is_displayed()
            print("element displayed: " + str(ele))
        except:
            print('here in')



a = FindElements()
a.test2()