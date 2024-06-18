from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class testOfCheckbox():
    def test(self):
        baseURL = "https://www.myntra.com/men-tshirts"
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")

        driver = webdriver.Chrome(options=options)
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)
        moreBrands =driver.find_element(By.XPATH,"//div[@class='brand-more']")
        moreBrands.click()
        # elements = driver.find_elements(By.XPATH,"//ul[@class='FilterDirectory-list']/li/label/input[@type='checkbox']")
        elements = driver.find_elements(By.XPATH,"//ul[@class='FilterDirectory-list']/li/label/div[@class='common-checkboxIndicator']")
        print(len(elements))
        length = len(elements)
        for i in range(0,length):
            elements[i].click()
            time.sleep(2)
            # print(elements[i].get_attribute("value"))
            # name = str(elements[i].get_attribute("value"))
            # if(name[0] =='Y'):
            #     elements[i].click()
            #     time.sleep(2)
            # if(elements[i].is_selected()):
            #     print("Yes")



a = testOfCheckbox()
a.test()