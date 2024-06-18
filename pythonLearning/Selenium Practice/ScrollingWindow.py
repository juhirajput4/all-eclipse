from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ScrollingWindow():
    def Test(self):
        baseUrl = "https://letskodeit.teachable.com/courses"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        # by using javascript
        # 1. Scroll Down

        print(driver.execute_script("window.scrollBy(0,2000)"))
        time.sleep(4)



        # 2. Scroll Up
        driver.execute_script("window.scrollBy(0,-2000)")
        time.sleep(4)

        # 3. Scroll element in view
        element = driver.find_element(By.ID,"search-courses")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(4)
        driver.execute_script("window.scrollBy(0,-50)")
        time.sleep(4)

        # 4. By using webdriver function
        driver.execute_script("window.scrollBy(0,-2000)")
        time.sleep(6)
        location = element.location_once_scrolled_into_view
        print(location)
        time.sleep(6)

        driver.execute_script("window.scrollBy(0,-50)")
        time.sleep(4)



a = ScrollingWindow()
a.Test()