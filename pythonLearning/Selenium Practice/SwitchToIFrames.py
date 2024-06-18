from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToIFrames():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()
        # Switch to frame using id
        # driver.switch_to.frame("courses-iframe")

        # Switch to frame using name
        # driver.switch_to.frame("iframe-name")

        # Switch to frame using numbers
        driver.switch_to.frame(0)

        time.sleep(2)

        searchCourse = driver.find_element(By.XPATH, "//input[@id='search']")
        searchCourse.send_keys('Python')
        time.sleep(2)

        # Switch back to the Parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scroll(0,-1000);")
        time.sleep(2)

        enterName = driver.find_element(By.NAME, "enter-name")
        enterName.send_keys("juhi")
        time.sleep(2)

a = SwitchToIFrames()
a.test()