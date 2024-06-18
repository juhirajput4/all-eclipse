import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
import random
from generateIP import getProxies

class automate_YouTube():
    def test(self):
        baseURL = "https://www.youtube.com/watch?v=JuayXgKvdsk"
        ipList = getProxies()

        for item in ipList:
            op = webdriver.ChromeOptions()
            op.add_argument("--incognito")
            ip = '--proxy-server=' + item
            print('ip address', ip)
            op.add_argument(ip)

            driver = webdriver.Chrome(options=op)
            driver.maximize_window()
            driver.get(baseURL)
            time.sleep(3)

            # video_player = driver.find_element(By.CLASS_NAME, "ytp-play-button")
            time.sleep(3)
            # video_player.click()

            time.sleep(70)
            driver.close()


a = automate_YouTube()
view =0
while True:
    a.test()
    print('view',view)
    view = view +1
