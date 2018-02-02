# -*- coding: utf-8 -*-
from selenium import webdriver



import unittest, time, re

class EEFiles(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("F:\\AUTOMATION\\Browsers\\Chrome\\chromedriver_win32\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "http://hotel-test.equalexperts.io/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_e_e_files(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("firstname").send_keys("new")
        driver.find_element_by_id("lastname").send_keys("user")
        driver.find_element_by_id("totalprice").send_keys("100")
        driver.find_element_by_id("checkin").click()
        driver.find_element_by_link_text("12").click()
        driver.find_element_by_id("checkout").click()
        driver.find_element_by_link_text("13").click()
        driver.find_element_by_css_selector("#form > div.row > div.col-md-1 > input[type=\"button\"]").click()
        driver.find_element_by_css_selector("#31985 > div.col-md-1 > input[type=\"button\"]").click()

        driver.find_element_by_id("firstname").send_keys("new")
        driver.find_element_by_id("lastname").send_keys("user")
        driver.find_element_by_id("totalprice").send_keys("-120")
        Select(driver.find_element_by_id("depositpaid")).select_by_visible_text("false")
        driver.find_element_by_id("checkin").click()
        driver.find_element_by_link_text("12").click()
        driver.find_element_by_id("checkout").click()
        driver.find_element_by_link_text("13").click()
        driver.find_element_by_css_selector("#form > div.row > div.col-md-1 > input[type=\"button\"]").click()
        driver.find_element_by_css_selector("#31986 > div.col-md-1 > input[type=\"button\"]").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
