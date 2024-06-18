from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AttributeValueElement():

    def test(self):
       driver = webdriver.Chrome()
       baseUrl = "https://www.facebook.com/"
       driver.maximize_window()
       driver.get(baseUrl)
       driver.implicitly_wait(10)

       pas = driver.find_element(By.ID, "pass")
       attribute_name = pas.get_attribute("class")
       print("The value of the type attribute is " + attribute_name)
       driver.close()

a = AttributeValueElement()
a.test()