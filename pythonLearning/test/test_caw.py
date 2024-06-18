from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class test_caw():
    def test(self):
        baseUrl = "https://www.att.com/buy/phones/apple-iphone-14.html"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(4)
        capacity = driver.find_elements(By.XPATH,"//fieldset[@id='Capacity']/div/div/label")
        for cap in capacity:
            text = cap.text()
            if text =="512 GB":
                cap.click()

a = test_caw()
a.test()


