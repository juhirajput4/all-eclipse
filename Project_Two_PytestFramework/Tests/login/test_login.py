from Pages.LoginClass.loginPageClass import loginPageClass

import time
import pytest
import unittest

@pytest.mark.usefixtures("setupDriver")
class loginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setUpMethod(self, setupDriver):
        self.lp = loginPageClass(self.driver)

    def test_Login(self):
        self.lp.logout()
        time.sleep(3)
        self.lp.login("juhi.rajput@cloudanalogy.com", "abcabc")
        time.sleep(3)

