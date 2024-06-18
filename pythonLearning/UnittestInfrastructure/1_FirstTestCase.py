# python 1_FirstTestCase.py
import unittest

class FirstTestCase(unittest.TestCase):
    @classmethod             # This is a decorator
    def setUpClass(cls):
        print("*#" *30)
        print("It will run only once before all tests")
        print("*#" * 30)

    def setUp(self):
        print("I will run once before every test")

    def test_method_A(self):
        print("test method A")

    def test_method_B(self):
        print("test method B")

    def tearDown(self):
        print("I will run after every test")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("It will run only once after all tests")
        print("*#" * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)


