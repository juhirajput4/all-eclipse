from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

class EXplicitWaitDemo():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        # driver.get(baseUrl)
        driver.execute_script("window.location = 'https://letskodeit.teachable.com'")

        wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")))
        element.click()
        email = wait.until(EC.visibility_of_element_located((By.ID, "email")))
        email.send_keys("test")


        # emailField = driver.find_element(By.ID, "email")
        # emailField.send_keys("test")

ff = EXplicitWaitDemo()
ff.test()