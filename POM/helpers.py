
from datetime import date, datetime, timedelta
import arrow as arrow

class helpers(object):

    def __init__(self, driver):
        self.driver = driver

    def get_dates(self):
        Todaysdate = arrow.now().format('YYYY-MM-DD')
        date1 = datetime.strptime(Todaysdate, "%Y-%m-%d")
        date2 = date1 + timedelta(days=1) # using checking date for tomorrow
        date3 = date1 + timedelta(days=6) # using checkout date as 5 days from booking date
        checkindate = datetime.strftime(date2, "%Y-%m-%d")
        checoutdate = datetime.strftime(date3, "%Y-%m-%d")

        return(checkindate,checoutdate)