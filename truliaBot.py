from selenium.common import NoSuchElementException
from bot import Bot
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TruliaBot(Bot):
    def __init__(self, driver, city, minimum_price, maximum_price, property_type):
        super().__init__(driver, city, minimum_price, maximum_price, property_type)

    def open_webpage(self):
        self.driver.get(self.get_formatted_url())
        assert "Page not found" not in self.driver.page_source

    def close_webpage(self):
        pass

    def set_property_type(self):
        if self.property_type == 'apartment':
            return 'APARTMENT,CONDO,COOP'
        elif self.property_type == 'house':
            return 'SINGLE-FAMILY_HOME'
        elif self.property_type == 'townhome':
            return 'TOWNHOUSE'
        elif self.property_type == 'townhome':
            return 'ANY'

    def get_formatted_url(self):
        self.city.replace('-', '_')
        return f'https://www.trulia.com/for_sale/{self.city},FL/{self.minimum_price}-{self.maximum_price}_price' \
               f'/{self.set_property_type()}_type/ '

    # TODO
    def get_listings(self):
        pass
