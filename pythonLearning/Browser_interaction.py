from selenium import webdriver
import time

class browserInteraction():
    def test(self):
        baseURL = "https://www.facebook.com/login/"

        #driver = webdriver.Chrome(executable_path="C:\\Users\\Cloud Analogy\\Desktop\\chromedriver.exe")
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.maximize_window()
        time.sleep(4)
        title = driver.title
        print("title of the page is"+ title)

        #get current url
        currentURL= driver.current_url
        time.sleep(4)
        print("currentURL of the page is" + currentURL)
        driver.refresh()
        print("refresh first time")
        time.sleep(4)
        driver.get(currentURL)
        time.sleep(4)

        #browser back
        driver.back()
        time.sleep(4)
        driver.forward()
        time.sleep(4)

        #get page source

        pageSource = driver.page_source

        #browser close(close only tab)/quit(close browser)
        driver.close()

a = browserInteraction()
a.test()