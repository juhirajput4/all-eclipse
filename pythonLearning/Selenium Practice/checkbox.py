from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

class Checkbox():

    def test(self):
        baseurl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        option1_checkbox = driver.find_element(By.CSS_SELECTOR,"#bmwcheck")
        option1_checkbox.click()
        print("check option1 is checked or not?"+ str(option1_checkbox.is_selected()))
        time.sleep(4)
        print("check option1 is checked or not?" + str(option1_checkbox.is_selected()))
        time.sleep(4)

    def test1(self):
        baseurl = "https://courses.letskodeit.com/practice"
        #driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        # driver.implicitly_wait(10)

        option_checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        print(len(option_checkbox))
        for i in option_checkbox:
            print(str(i.is_displayed()))
            if i.is_displayed() is True:
                i.click()
        print('Out of loop')
        # time.sleep(10)
        # driver.close()


    def test2(self):
        baseurl = "https://www.google.com/"
        #driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        gm = driver.find_element(By.LINK_TEXT,"Gmail")
        if gm is not None:
            print('Element -found')
        print(gm.text)
        print(gm.get_attribute("href"))

# Alternate checkbox checked
    def test3(self):
        baseurl = "https://courses.letskodeit.com/practice"
        #driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        # driver.implicitly_wait(10)

        option_checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @name='cars']")
        print(len(option_checkbox))
        length = len(option_checkbox)
        for i in option_checkbox:
            if i.is_selected() == False:
                i.click()
        """
        for i in range(1,length,2):
            if option_checkbox[i].is_displayed() is True:
                option_checkbox[i].click()
        """

        print('Out of loop')
        # time.sleep(10)
        driver.close()

a = Checkbox()
a.test3()
#driver.close()