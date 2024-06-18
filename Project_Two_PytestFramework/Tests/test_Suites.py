import unittest
from Tests.courses.test_usingNavigation import Test_register_courses
from Tests.login.test_login import loginTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(Test_register_courses)
tc2 = unittest.TestLoader().loadTestsFromTestCase(loginTest)

smokeTest = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(smokeTest)
