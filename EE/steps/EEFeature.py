from datetime import date, datetime, timedelta
import arrow as arrow
from behave import *
from POM.AutomationDriver import AutomationDriver
from POM.bookingpage import bookingpage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui

step_matcher("re")

@given("we are able to access the url")
def step_impl(context):
    driver = AutomationDriver.driver
    base_url = "http://hotel-test.equalexperts.io/"
    driver.get(base_url)
    driver.implicitly_wait(30)

@when("I am able to save the details (?P<First_Name>.+) (?P<Surname>.+) (?P<Price>.+) (?P<deppaid>.+)")
def step_impl(context, First_Name, Surname, Price, deppaid):

    driver = AutomationDriver.driver

    Todaysdate = arrow.now().format('YYYY-MM-DD')
    date1 = datetime.strptime(Todaysdate, "%Y-%m-%d")
    date2 = date1 + timedelta(days=1) # using checking date for tomorrow
    date3 = date1 + timedelta(days=6) # using checkout date as 5 days from booking date
    CheckinDate = datetime.strftime(date2, "%Y-%m-%d")
    ChecoutDate = datetime.strftime(date3, "%Y-%m-%d")

    booking = bookingpage(driver)

    booking.firstname(First_Name)
    booking.surname(Surname)
    booking.totalprice(Price)

    if deppaid == "Yes":
        booking.depositepaid()
    else:
        booking.depositnotpaid()

    booking.checkin(CheckinDate)
    booking.checkout(ChecoutDate)
    booking.savebooking()

@then("Application works fine")
def step_impl(context):
    print("users created successfully")
    pass


@then("I am able to delete the details (?P<First_Name>.+) (?P<Surname>.+) (?P<Price>.+)")
def step_impl(context, First_Name, Surname, Price):
    driver = AutomationDriver.driver
    try:
        ui.WebDriverWait(driver, 10, poll_frequency=0.1).until(
            EC.visibility_of_element_located((By.XPATH, ".//*[@id='form']/div/div[7]")))
    except TimeoutError as e:
        print("Page not fully loaded. Please check")
    driver.implicitly_wait(10)
    table= driver.find_element_by_id("bookings")
    rows = table.find_elements_by_class_name("row")
    print("length = " + str(len(rows)) + "\n")
    for row in rows :
        first_name = row.text.split("\n")[0]
        surname = row.text.split("\n")[1]
        price = row.text.split("\n")[2]
        # deposit = row.text.split("\n")[3]
        # checkin = row.text.split("\n")[4]
        # checkout = row.text.split("\n")[5]
        # print(first_name)
        if ( first_name == First_Name and surname == Surname and price == Price):
            row.find_element_by_tag_name("input").click()
            # row.find_element_by_css_selector("input[type='button']").click()
            print(first_name + surname + " successfully deleted")
            # break



