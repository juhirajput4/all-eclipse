from _ast import Assert

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

class playwright():
    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.google.com/")
        search = driver.find_element(By.NAME,"q")
        search.send_keys("playwright")
        search.send_keys(Keys.RETURN)
        link = driver.find_element(By.XPATH,"(//div[@class=\"g\"])[2]/div/div/div/a/h3")
        actualLinkText =  link.text
        expectedText = "Playwright: Fast and reliable end-to-end testing for modern ..."
        # Assert.assertEquals(expectedText, actualLinkText)
        assert actualLinkText == expectedText
        print("+++++++++++++++")

a = playwright()
a.test()
