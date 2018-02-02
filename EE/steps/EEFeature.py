from behave import *
from POM.bookingpage import bookingpage
from POM.helpers import helpers

step_matcher("re")

@given("we are able to access the url")
def step_impl(context):
    driver = context.browser
    base_url = "http://hotel-test.equalexperts.io/"
    driver.get(base_url)

@when("I am able to save the details (?P<First_Name>.+) (?P<Surname>.+) (?P<Price>.+) (?P<deppaid>.+)")
def step_impl(context, First_Name, Surname, Price, deppaid):

    driver = context.browser

    dates = helpers(driver)
    checkin_date, checkout_date = dates.get_dates()

    booking = bookingpage(driver)
    booking.firstname(First_Name)
    booking.surname(Surname)
    booking.totalprice(Price)

    if deppaid == "Yes":
        booking.depositepaid()
    else:
        booking.depositnotpaid()

    booking.checkin(checkin_date)
    booking.checkout(checkout_date)
    booking.savebooking()

@then("Application works fine")
def step_impl(context):
    print("users created successfully")

@then("I am able to delete the details (?P<First_Name>.+) (?P<Surname>.+) (?P<Price>.+)")
def step_impl(context, First_Name, Surname, Price):
    driver = context.browser
    booking = bookingpage(driver)
    booking.checkpageload()
    booking.deleterows(First_Name, Surname, Price)