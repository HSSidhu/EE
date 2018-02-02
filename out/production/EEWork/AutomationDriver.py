from selenium import webdriver

class AutomationDriver(object):

    # driver = webdriver.Chrome("F://AUTOMATION//Browsers//Chrome//chromedriver_win32//chromedriver.exe")
    path = "F:\\AUTOMATION\\00 Completed Projects\\EEWorkspace\\EE_WebsiteAutomation\\Hotel_Booking\\webdriver"
    driver = webdriver.Chrome(path + "\\chromedriver.exe")
    driver.maximize_window()

