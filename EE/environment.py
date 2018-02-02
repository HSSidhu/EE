import collections
from selenium import webdriver
import xlrd
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

WindowSize = collections.namedtuple('WindowSize', 'width height')
WINDOW_SIZE = WindowSize(width=1920, height=1080)

DEFAULT_PAGE_WAIT_IN_SECONDS = 10

def before_all(context):
    print('>> before_all')  # u can choose OS here if u want
    _output_os_details()
    if choose_browser(context) == "chrome":
        _open_chrome_for_windows(context)
    elif choose_browser(context)== "ie":
        _open_ie_for_windows(context)

    _set_default_page_wait_in_seconds(context.browser)

def _output_os_details():
    import platform

    print('\n>> os details <<')
    print('>> uname: {}'.format(platform.uname()))
    print('>> dist: {}'.format(platform.dist()))
    print('>> os details <<\n')

def _open_chrome_for_windows(context):
    path = "F:\\FNC-Workspace\\FNC\\fnc-development-environment\\apps\\funeral-director-frontend-tests\\Drivers"
    context.browser = webdriver.Chrome(path + "\\chromedriver.exe")
    context.browser.maximize_window()

def _open_ie_for_windows(context):
    capabilities = DesiredCapabilities.INTERNETEXPLORER
    capabilities.pop("platform", None)
    capabilities.pop("version", None)
    # driver = webdriver.Ie(executable_path="F:\\AUTOMATION\Browsers\\IEDriver\\BIT-32\\IEDriverServer.exe", capabilities=capabilities)
    path = "F:\\FNC-Workspace\\FNC\\fnc-development-environment\\apps\\funeral-director-frontend-tests\\Drivers"
    context.browser = webdriver.Ie(path + "\\IEDriverServer.exe")
    context.browser.delete_all_cookies()

def _set_default_page_wait_in_seconds(browser):
    browser.implicitly_wait(DEFAULT_PAGE_WAIT_IN_SECONDS)

def after_all(context):
    print('>> after_all')

    print('>> closing chrome')
    context.browser.quit()

    try:
        context.display.stop()
        print('>> stopping pyvirtualdisplay')
    except AttributeError:
        pass

def choose_browser(context):
    # test_data_sheet = "location of EXCEL on the machine"
    # users_test_data = xlrd.open_workbook(test_data_sheet)
    # allusers = users_test_data.sheet_by_name(give the worksheet name and then in below step do the same )
    context.browser_name = "chrome"  # u can use different browsers here as well but the code might have to be
    # modfied as browsers behave diferently to each other
    return(context.browser_name)