import booking.constants as const
import os
from selenium import  webdriver


class Booking(webdriver.Chrome):
    def __int__(self, driver_path='C:\Selenium_Driver'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()

    def land_first_page(self):
        self.get(const.BASE_URL)