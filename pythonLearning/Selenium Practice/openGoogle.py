from selenium import webdriver
from selenium.webdriver.common.by import By

class openGoogle():

    def test(self):
        baseUrl= "https://www.google.com/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        inputBox = driver.find_element(By.NAME,"q")
        inputBox.send_keys("python course")
        driver.find_element(By.XPATH,"(//input[@value='Google Search'])[2]").click()

obj = openGoogle()
obj.test()