from selenium import webdriver
from truliaBot import TruliaBot
from realtorDotComBot import RealtorDotComBot
from searchDetails import SearchDetails


class Facade:
    def __init__(self):
        self.search_details = SearchDetails()
        self.city = None
        self.minimum_price = None
        self.maximum_price = None
        self.property_type = None

    def get_search_information(self):
        self.search_details = SearchDetails()
        self.city = self.search_details.city_query()
        self.minimum_price = self.search_details.min_price_query()
        self.maximum_price = self.search_details.max_price_query()
        self.property_type = self.search_details.property_type_query()

    def comfirm_user_input(self):
        details_confirmation = False
        while not details_confirmation:
            print("Please enter the following details to search for properties: ")

            confirmation = input(f'\nPlease confirm the details of your search:\n'
                                 f'City: {self.city}\n'
                                 f'Minimum price: {self.minimum_price}\n'
                                 f'Maximum price: {self.maximum_price}\n'
                                 f'Property type: {self.property_type}\n\n'
                                 f'To confirm and search press \'Y\', to re-enter the search information '
                                 f'press \'N\': ').lower()

            if confirmation != 'y':
                print('\nPlease enter the search details again.\n')

            else:
                details_confirmation = True
                break

    def get_realtor_listings(self):
        driver = webdriver.Firefox()
        realtor_dot_com_bot = RealtorDotComBot(driver, self.city, self.minimum_price, self.maximum_price,
                                               self.property_type)
        realtor_dot_com_bot.open_webpage()
        realtor_dot_com_bot.get_listings()
        driver.close()

    def get_trulia_listings(self):
        driver = webdriver.Firefox()
        trulia_bot = TruliaBot(driver, self.city, self.minimum_price, self.maximum_price,
                               self.property_type)
        trulia_bot.open_webpage()
        trulia_bot.get_listings()
        driver.close()

    def run_realtor_bot(self):
        self.get_search_information()
        self.comfirm_user_input()
        self.get_realtor_listings()

    def run_trulia_bot(self):
        self.get_search_information()
        self.comfirm_user_input()
        self.get_trulia_listings()
