from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

class DragAndDrop():
    def test(self):
        baseUrl = "https://jqueryui.com/droppable/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()

        driver.switch_to.frame(0)
        fromElement = driver.find_element(By.ID,"draggable")
        toElement = driver.find_element(By.ID,"droppable")

        try:
            action = ActionChains(driver)
            # action.drag_and_drop(fromElement, toElement).perform()
            action.click_and_hold(fromElement).move_to_element(toElement).release().perform()

            time.sleep(2)
            print("drag and drop pass on the element")

        except:
            print("drag and drop failed on the element")


a = DragAndDrop()
a.test()