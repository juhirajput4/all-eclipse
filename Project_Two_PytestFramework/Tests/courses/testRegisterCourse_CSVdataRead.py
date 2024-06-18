from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.LoginClass.loginPageClass import loginPageClass
import time
from Pages.CourseClass.coursePageClass import coursePageClass
from ddt import ddt, data, unpack
import unittest, pytest
from utilities.readCSVData import getCSVdata

@pytest.mark.usefixtures("setupDriver")
@ddt
class Test_register_courses(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetUp(self, setupDriver):
        self.co = coursePageClass(self.driver)

    @pytest.mark.run(order = 1)
    @data(*getCSVdata("C:/Users/Cloud Analogy/PycharmProjects/Project_Two_PytestFramework/data.csv"))
    @unpack
    def test_invalidEnrollment(self, cName, card, date, cvv, country):

        self.co.course(courseName=cName, cardNumber=card, exDate=date , securityCode=cvv, ele=country)
        time.sleep(3)
        msg = self.driver.find_element(By.XPATH, "//li[@class='card-no cvc expiry text-danger']/span")
        print(msg.text)
        if msg.text.__contains__("declined"):
            print("payment is declined")
            assert True == True


