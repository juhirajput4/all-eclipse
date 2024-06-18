from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DropdownDynamic():

    def test(self):
       driver = webdriver.Edge()
       baseUrl = "https://www.goibibo.com/"
       driver.maximize_window()
       driver.get(baseUrl)
       driver.implicitly_wait(4)
       fromCity = driver.find_element(By.XPATH, "(//div[@class='sc-ksdxgE dvdvQX fswFld '])[1]")
       fromCity.click()

       driver.find_element(By.XPATH, "//div[@class='sc-jJoQJp echhfS']/input").send_keys("Del")
       # fromCity.find_element(By.TAG_NAME,"input").send_keys("del")
       suggestions = driver.find_elements(By.XPATH,"//ul[@id='autoSuggest-list']/li")
       for item in suggestions:
          print(item.text)
          if "Delhi" in item.text:
             item.click()
             # we need break because if we click any item from suggestions, suggestion list from DOM is removed
             break

       time.sleep(3)

a = DropdownDynamic()
a.test()



