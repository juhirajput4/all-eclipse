from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BetCity():
    def test(self):
        baseURL = "https://www.betcity.nl/sportsbook#event/1019168398"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(5)

        cookies = driver.find_element(By.XPATH,"//button[@id='CybotCookiebotDialogBodyButtonAccept']")
        cookies.click()

        doubleChance = driver.find_element(By.XPATH,"(//div[@class='KambiBC-bet-offer-subcategory__container']/div/div/div[@class='KambiBC-outcomes-list__column']/button)[6]")
        doubleChanceText = doubleChance.text.split()[1]

        voidOnATie = driver.find_element(By.XPATH,"(//div[@class='KambiBC-bet-offer-subcategory__container']/div/div/div[@class='KambiBC-outcomes-list__column']/button)[11]")
        voidOnATieText = voidOnATie.text.split()[1]

        if doubleChanceText == "1.11" and voidOnATieText == "1.15":
            doubleChance.click()
            voidOnATie.click()
            xpath = driver.find_element(By.XPATH,"//input[@id='mod-KambiBC-betslip-stake-input-combination']")
            xpath.send_keys("0.1")
            time.sleep(10)


        else:
            print("--- Conditions are not matching ---")


a = BetCity()
a.test()