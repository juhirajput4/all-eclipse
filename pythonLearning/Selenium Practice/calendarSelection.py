from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class calendarSelection():

    def test(self):
       driver = webdriver.Edge()
       baseUrl = "https://www.expedia.co.in/"
       driver.maximize_window()
       driver.get(baseUrl)
       driver.implicitly_wait(2)

       # Entering the user name
       flightTab = driver.find_element(By.XPATH,"//a[@aria-controls='wizard-flight-pwa']")
       flightTab.click()
       departingField = driver.find_element(By.XPATH, "(//button[@data-stid='open-date-picker'])[1]")
       departingField.click()
       selectDate = driver.find_element(By.XPATH,"(//button[@data-day='30'])[1]")
       selectDate.click()
       time.sleep(4)

    def test2(self):
       driver = webdriver.Edge()
       baseUrl = "https://www.expedia.co.in/"
       driver.maximize_window()
       driver.get(baseUrl)
       driver.implicitly_wait(2)

       # Entering the user name
       flightTab = driver.find_element(By.XPATH,"//a[@aria-controls='wizard-flight-pwa']")
       flightTab.click()
       departingField = driver.find_element(By.XPATH, "(//button[@data-stid='open-date-picker'])[1]")
       departingField.click()
       calMonth = driver.find_element(By.XPATH,"(//div[@class='uitk-date-picker-month'])[1]")
       allDate = calMonth.find_elements(By.TAG_NAME, "button")
       for date in allDate:

          if date.get_attribute("data-day")=="30":
             # print("juhi")
             date.click()
             time.sleep(4)
          print(date.get_attribute("aria-label"))

       time.sleep(4)

    def test3(self):
       driver = webdriver.Edge()
       baseUrl = "https://www.expedia.co.in/"
       driver.maximize_window()
       driver.get(baseUrl)
       driver.implicitly_wait(5)

       # Entering the user name
       flightTab = driver.find_element(By.XPATH, "//a[@aria-controls='wizard-flight-pwa']")
       flightTab.click()
       departingField = driver.find_element(By.XPATH, "(//button[@data-stid='open-date-picker'])[1]")
       departingField.click()
       selectDate = driver.find_element(By.XPATH, "(//button[@data-day='30'])[1]")
       selectDate.click()
       # returningField = driver.find_element(By.XPATH, "(//button[@data-stid='open-date-picker'])[2]")
       # returningField.click()
       returnDate = driver.find_element(By.XPATH, "(//button[@data-day='26'])[2]")
       returnDate.click()
       time.sleep(4)




a = calendarSelection()
a.test2()



