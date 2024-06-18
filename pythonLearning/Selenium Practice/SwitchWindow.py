from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchWindow():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()

        # Find parent handle - Main window
        parentHandle = driver.current_window_handle
        print("parentHandle" + parentHandle)

        # Find open window button and click it
        driver.find_element(By.ID,'openwindow').click()
        time.sleep(2)

        # Find all the handles, these should be two handles after clicking open window button
        handles = driver.window_handles

        # Switch window and search cources
        for handle in handles:
            print("handle " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("current handles " + handle)
                searchCourse = driver.find_element(By.XPATH,"//input[@id='search']")
                searchCourse.send_keys('Python')
                
                time.sleep(4)
                driver.close()
                break

        # Switch to Parent window
        driver.switch_to.window(parentHandle)
        enterName = driver.find_element(By.NAME,"enter-name")
        enterName.send_keys("juhi")

        time.sleep(3)
        driver.close()


a = SwitchWindow()
a.test()