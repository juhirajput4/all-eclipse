import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class automate_YouTube():
    def test(self):
        baseURL = "https://www.youtube.com/watch?v=JuayXgKvdsk"
        op = webdriver.ChromeOptions()
        op.add_argument("--incognito")
        driver = webdriver.Chrome(options=op)
        driver.maximize_window()
        driver.get(baseURL)
        time.sleep(3)

        video_player = driver.find_element(By.CLASS_NAME, "ytp-play-button")
        time.sleep(3)

        # click the video player to give it focus
        video_player.click()

        # wait for the video to load and start playing
        time.sleep(5)

        # send spacebar key to pause the video
        #video_player.send_keys(Keys.SPACE)

        # wait for 2 seconds
        time.sleep(2)

        # send spacebar key again to resume playing the video
        #video_player.send_keys(Keys.SPACE)
        time.sleep(70)
        driver.close()


a = automate_YouTube()
view =0
while True:
    a.test()
    a.test()
    a.test()
    a.test()
    a.test()

    print('view',view)
    view = view +1
    time.sleep(3)
