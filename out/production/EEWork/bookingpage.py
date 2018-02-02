import objects as objects
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys


class bookingpage(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def firstname(self, fname):
        self.driver.find_element_by_id("firstname").send_keys(fname)

    def surname(self, sname):
        self.driver.find_element_by_id("lastname").send_keys(sname)

    def totalprice(self, price):
        self.driver.find_element_by_id("totalprice").send_keys(price)

    def checkin(self, checkindate):
        self.driver.find_element_by_xpath(".//*[@id='checkin']").send_keys(checkindate)

    def checkout(self, checkoutdate):
        self.driver.find_element_by_xpath(".//*[@id='checkout']").send_keys(checkoutdate)

    def depositepaid(self):
        self.driver.find_element_by_xpath(".//*[@id='depositpaid']/option[1]").click()

    def depositnotpaid(self):
        self.driver.find_element_by_xpath(".//*[@id='depositpaid']/option[2]").click()

    def savebooking(self):
        self.driver.find_element_by_xpath(".//*[@id='form']/div/div[7]").click()

        #ActionChains(self.driver).move_to_element(elem).click().perform()


