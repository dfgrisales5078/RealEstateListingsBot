from selenium.common import NoSuchElementException
from bot import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class RealtorDotComBot(Bot):
    def __init__(self, driver, city, minimum_price, maximum_price, property_type):
        super().__init__(driver, city, minimum_price, maximum_price, property_type)

    def open_webpage(self):
        self.driver.get(self.get_formatted_url())
        assert "Page not found" not in self.driver.page_source

    def close_webpage(self):
        pass

    def set_property_type(self):
        if self.property_type == 'apartment':
            return 'condo'
        elif self.property_type == 'house':
            return 'single-family-home'
        else:
            return self.property_type

    def get_formatted_url(self):
        return f'https://www.realtor.com/realestateandhomes-search/{self.city}_Fl/' \
               f'type-{self.set_property_type()}/price-{self.minimum_price}-{self.maximum_price}'

    # TODO
    def get_listings(self):
        pass
