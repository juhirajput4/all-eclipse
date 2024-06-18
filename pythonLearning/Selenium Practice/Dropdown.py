from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Dropdown():

    def test(self):
        # baseUrl = "https://courses.letskodeit.com/practice"
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()

        elements = driver.find_element(By.ID,"carselect")
        sel = Select(elements)

        sel.select_by_index(1)
        time.sleep(2)

        sel.select_by_value("honda")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        time.sleep(2)

        sel.select_by_index("2")

a = Dropdown()
a.test()