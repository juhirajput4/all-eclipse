import unittest
from test_class1 import test_class1
from test_class2 import test_class2

#Get all test from test_class1 and test_class2
tc1 = unittest.TestLoader().loadTestsFromTestCase(test_class1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(test_class2)

# Create a test suits combine test_class1 and test_class2
smoke_test = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(smoke_test)