import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class amazon():
    def test(self):
        baseUrl = "https://www.amazon.in/b/?_encoding=UTF8&node=27063338031&pf_rd_r=AGV7YHRKFZZ0KGXJJK4Y&pf_rd_p=2723ecbd-91e0-4fb1-9740-39850db10603&pd_rd_r=76812b35-341c-4ddc-bad4-8841440df701&pd_rd_w=EPPpE&pd_rd_wg=kRHFT&ref_=pd_gw_unk"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        a = ActionChains(driver)
        m = driver.find_element(By.CLASS_NAME,"nav-a nav-a-2 ")
        a.move_to_element(m).perform()
        n = driver.find_element(By.LINK_TEXT,"Your Prime Video")
        a.move_to_element(n).click().perform()
        time.sleep(3)


b = amazon()
b.test()
