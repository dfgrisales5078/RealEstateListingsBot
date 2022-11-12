from selenium.common import NoSuchElementException
from bot import Bot
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class GreaterFortMyersBot(Bot):
    def __init__(self, driver, city_or_zipcode, minimum_price, maximum_price, property_type):
        super().__init__(driver, city_or_zipcode, minimum_price, maximum_price, property_type)

    def open_webpage(self, url):
        self.driver.get(url)

    def close_webpage(self):
        pass

    def set_city_or_zipcode(self):
        try:
            search_input_box = WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[8]/section/div['
                                                                           '2]/div/div/div[2]/div[2]/div[2]/div['
                                                                           '1]/div[1]/div/input')))
            search_input_box.click()
            search_input_box.send_keys(self.city_or_zipcode)
            search_input_box.send_keys(Keys.ENTER)
        except NoSuchElementException as Error:
            print(f'Could not search input box: {Error}')

        try:
            search_button = WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[8]/section/div['
                                                                           '2]/div/div/div[2]/div[2]/div[2]/div['
                                                                           '1]/div[1]/div/span/button')))
            search_button.click()
        except NoSuchElementException as Error:
            print(f'Could not search button: {Error}')

    # TODO
    def set_property_type(self):
        pass

    def set_price_ranges(self):
        sleep(2)
        try:
            minimum_price_input_box = WebDriverWait(self.driver, 25).until(
                expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="minItem_39225504"]')))
            minimum_price_input_box.click()
            sleep(2)
            minimum_price_input_box.send_keys(self.minimum_price)
        except NoSuchElementException as Error:
            print(f'Could not find minimum input box: {Error}')

        # try:
        #     maximum_price_input_box = WebDriverWait(self.driver, 20).until(
        #         expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="maxInput_39225504"]')))
        #     maximum_price_input_box.click()
        #     maximum_price_input_box.send_keys(self.maximum_price)
        #     maximum_price_input_box.send_keys(Keys.ENTER)
        #
        # except NoSuchElementException as Error:
        #     print(f'Could not find maximum input box: {Error}')

    def get_listings(self):
        self.set_price_ranges()
        self.set_city_or_zipcode()
