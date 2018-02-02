# from _ast import List
# from datetime import date, datetime, timedelta
# from itertools import count
#
# import arrow as arrow
# import selenium
# from _pytest import unittest
# from behave import *
# from POM.AutomationDriver import AutomationDriver
# from POM.bookingpage import bookingpage
#
#
# use_step_matcher("re")
#
# @given("we are able to access the url (?P<url>.+)")
# def step_impl(context, url):
#     driver = AutomationDriver.driver
#     #base_url = "hhttp://hotel-test.equalexperts.io/"
#     driver.get(url)
#     driver.implicitly_wait(30)
#
# @when("I am able to save the details (?P<First_Name>.+) (?P<Surname>.+) (?P<Price>.+) (?P<deppaid>.+)(?P<url>.+)")
# def step_impl(context, First_Name, Surname, Price, deppaid, url):
#
#     driver = AutomationDriver.driver
#
#     Todaysdate = arrow.now().format('YYYY-MM-DD')
#     date1 = datetime.strptime(Todaysdate, "%Y-%m-%d")
#     date2 = date1 + timedelta(days=1) # using checking date for tomorrow
#     date3 = date1 + timedelta(days=6) # using checkout date as 5 days from booking date
#     CheckinDate = datetime.strftime(date2, "%Y-%m-%d")
#     ChecoutDate = datetime.strftime(date3, "%Y-%m-%d")
#
#     booking = bookingpage(driver)
#
#     booking.firstname(First_Name)
#     booking.surname(Surname)
#     booking.totalprice(Price)
#
#     if deppaid == "Yes":
#         booking.depositepaid()
#     else:
#         booking.depositnotpaid()
#
#     booking.checkin(CheckinDate)
#     booking.checkout(ChecoutDate)
#     #booking.savebooking()
#
# @then("Application works fine")
# def step_impl(context):
#     print("hello")
# #
# # @then("I am able to delete the details (?P<First_Name>.+) (?P<Surname>.+) (?P<Price>.+)")
# # def step_impl(context, First_Name, Surname, Price):
# #     numb = 0
# #     driver = AutomationDriver.driver
# #     b = 2
# #     value = "failure"
# #     numb = driver.find_elements_by_xpath(".//*[@id='bookings']/div/div[1]")
# #     numb1 = driver.find_elements_by_class_name("row")
# #     items = []
# #     #items.append(driver.find_elements_by_class_name("row"))
# #     items.append(driver.find_elements_by_xpath(".//*[@id='bookings']/div/div[1]"))
# #     print(items.__sizeof__())
# #
# #     # print(list)
# #     # print(len(numb))
# #     # print(len(numb1))
# #     # print(len(numb2))
# #
# #     while ( b <= 5):
# #         a = str(b)
# #         elem1 = driver.find_element_by_xpath(".//*[@id='bookings']/div["+a+"]/div[1]").text
# #         elem2 = driver.find_element_by_xpath(".//*[@id='bookings']/div["+a+"]/div[2]").text
# #         # elem3 = driver.find_element_by_xpath(".//*[@id='bookings']/div["+a+"]/div[3]").text
# #         # if elem1 == First_Name and elem2 == Surname and elem3 == Price :
# #         #         driver.find_element_by_xpath(".//*[@id='bookings']/div["+a+"]/div[7]").click()
# #         #         value = "success"
# #         #         b = int(a)  # this will ensure that any previous entry of same name and price will be deleted
# #         # else:
# #         #     b=b+1
# #         #
# #         # if value == "success" :
# #         #     print("Booking deleted successfully")
# #         # else:
# #         #     print("Booking do not exist")
# #
# #
