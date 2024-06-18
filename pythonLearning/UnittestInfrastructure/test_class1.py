import unittest

class test_class1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("*#" * 30)
        print("class 1 -> It will run only once before all tests")
        print("*#" * 30)

    def setUp(self):
        print("class 1 -> I will run once before every test")

    def test_method_A(self):
        print("class 1 -> test method A")

    def test_method_B(self):
        print("class 1 -> test method B")

    def tearDown(self):
        print("class 1 -> I will run after every test")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("class 1 -> It will run only once after all tests")
        print("*#" * 30)



if __name__ == '__main__':
    unittest.main(verbosity=2)