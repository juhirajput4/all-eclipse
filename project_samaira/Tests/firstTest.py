from selenium import webdriver
import time
from castro import Castro

from Base.login import Login
from Pages.Home_Page.provider_portal_home import ProviderPortal

rec = Castro(output_path='test.mp4',framerate=10)
rec.start()

driver = webdriver.Chrome()
lp = Login(driver)
# driver.get('https://biotheranostics--lisqa.sandbox.lightning.force.com/lightning/n/BTX_Home')

lp.login_to_dashboard('https://biotheranostics--lisqa.sandbox.my.site.com/s/login/?ec=302&startURL=%2Fs%2F')

pp = ProviderPortal(lp.driver)
pp.click_unsumbitted_request()
time.sleep(4)
pp.find_CTID_in_Table()
time.sleep(2)
pp.edit_form()
time.sleep(2)
pp.enter_sex()
pp.enter_dob()
pp.enter_bill_to()
time.sleep(2)
pp.enter_hospital_status()
time.sleep(2)
pp.press_save()
time.sleep(15)
pp.fomalities()

time.sleep(4)
rec.stop()
print('767676')

driver.close()





















