from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.filter_PageClass import filter_PageClass
import unittest

class test_filter_testClass(unittest.TestCase):
    def test_applyFilter(self):
        baseUrl = "https://coinmarketcap.com/"
        driver = webdriver.Chrome("C:/Users/Cloud Analogy/PycharmProjects/Project_One/venv/Scripts/chromedriver.exe")
        driver.get(baseUrl)
        driver.maximize_window()
        fp = filter_PageClass(driver)
        fp.apllyFilter()


