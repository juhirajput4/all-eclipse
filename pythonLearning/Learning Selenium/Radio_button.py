from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Radio_button():
    def test(self):
        baseurl = "https://www.facebook.com/"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        #time.sleep(4)
        create_new_account = driver.find_element(By.XPATH,'//a[@rel="async"]')
        create_new_account.click()
        #time.sleep(4)
        male_radio_button = driver.find_element(By.XPATH,'//input[@value="2"]')
        male_radio_button.click()
        #time.sleep(4)
        print("checked male button is checked or not?" + str(male_radio_button.is_selected()))
        #time.sleep(4)
        custom_radio_button = driver.find_element(By.XPATH, '//input[@value="-1"]')
        custom_radio_button.click()
        #time.sleep(4)
        print("checked male button is checked or not?" + str(male_radio_button.is_selected()))
        driver.close()
a = Radio_button()
a.test()
