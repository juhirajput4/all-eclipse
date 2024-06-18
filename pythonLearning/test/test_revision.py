from selenium import webdriver
import unittest
class google(unittest.TestCase):
    def test(self):
        print("fcscsza")
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")

if __name__ == '__main__':
    unittest.main(verbosity=1)
