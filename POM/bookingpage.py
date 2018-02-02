from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui


class bookingpage(object):

    def __init__(self, driver):
        self.driver = driver

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

    def checkpageload(self):
        try:
            self.driver.implicitly_wait(20)
            ui.WebDriverWait(self.driver, 20, poll_frequency=0.5).until(
                EC.visibility_of_element_located((By.XPATH, ".//*[@id='form']/div/div[7]")))
        except TimeoutError as e:
            print("Page not fully loaded. Please check")
            self.driver.close()

    def deleterows(self, First_Name, Surname, Price):

        table= self.driver.find_element_by_id("bookings")
        # rows = table.find_elements_by_class_name("row")
        # print("\n" +"Total Elements  = " + str(len(rows)) + "\n")
        for row in table.find_elements_by_class_name("row") :
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
                break


