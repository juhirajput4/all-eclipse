from selenium import webdriver
import time

class Chrome_windows():

    def test(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\Cloud Analogy\\Desktop\\chromedriver.exe")
        driver.get("https://www.google.com/")
        driver.maximize_window()
        time.sleep(4)
        driver.quit()

a = Chrome_windows()
a.test()