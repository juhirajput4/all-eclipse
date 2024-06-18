from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class mouseHoverActions():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()

        driver.execute_script("window.scroll(0, 600)")
        time.sleep(2)
        mouseHover = driver.find_element(By.ID,"mousehover")
        top = driver.find_element(By.XPATH,"//a[text()='Top']")
        try:
            action = ActionChains(driver)
            action.move_to_element(mouseHover).perform()
            time.sleep(2)
            print("mouse hovered on element")
            action.move_to_element(top).click().perform()
            time.sleep(2)
            print("go to the top")
        except:
            print("mouse hovered failed on the element")





a = mouseHoverActions()
a.test()