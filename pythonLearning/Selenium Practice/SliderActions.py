from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class SliderActions():
    def test(self):
        baseUrl = "https://jqueryui.com/slider/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()

        driver.switch_to.frame(0)
        element = driver.find_element(By.XPATH, "//div[@id='slider']/span")

        try:
            action = ActionChains(driver)
            action.drag_and_drop_by_offset(element, 100, 0).perform()
            time.sleep(2)
            print("drag and drop are pass the element")
        except:
            print("drog and drop are failed on the element")




a = SliderActions()
a.test()