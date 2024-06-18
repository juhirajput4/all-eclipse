from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class alertPopUp():
    def Test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()
        enterName = driver.find_element(By.NAME, "enter-name")
        enterName.send_keys("juhi")

        # for alert button
        driver.find_element(By.ID,"alertbtn").click()
        time.sleep(2)

        # switch to alert pop-up
        alrt = driver.switch_to.alert
        alrt.accept()

    def Test2(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()


        enterName = driver.find_element(By.NAME, "enter-name")
        enterName.send_keys("juhi")

        # for alert button
        driver.find_element(By.ID,"confirmbtn").click()
        time.sleep(2)

        # switch to alert pop-up
        alrt = driver.switch_to.alert

        # for click on Ok button
        alrt.accept()


        enterName1 = driver.find_element(By.NAME, "enter-name")
        enterName1.send_keys("juhi")

        # for alert button
        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(2)

        # switch to alert pop-up
        alrt = driver.switch_to.alert
        print(alrt.text)
        # if alrt.text == "Hello juhi, Are you sure you want to confirm?":
        if "Hello juhi" in alrt.text:

            print("showing correct text")
        # for click on Ok button
        alrt.dismiss()


a = alertPopUp()
a.Test()