from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Checkbox_check():
    def test(self):
        baseurl = "https://www.rahulshettyacademy.com/AutomationPractice/"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        option1_checkbox = driver.find_element(By.CSS_SELECTOR,"#checkBoxOption1")
        option1_checkbox.click()
        print("check option1 is checked or not?"+ str(option1_checkbox.is_selected()))
        time.sleep(4)
        print("check option1 is checked or not?" + str(option1_checkbox.is_selected()))
        time.sleep(4)
        driver.close()

a = Checkbox_check()
a.test()