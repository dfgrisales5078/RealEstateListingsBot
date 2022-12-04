from datetime import datetime
from selenium import webdriver
from dataFormatter import DataFormatter
from realtorDotComWebScraper import RealtorDotComWebScraper
from searchDetails import SearchDetails
from truliaWebScraper import TruliaWebScraper
from homesDotComWebScraper import HomesDotComWebScraper


class Facade:
    def __init__(self):
        self.search_details = SearchDetails()
        self.data_formatter = DataFormatter()
        self.city = None
        self.minimum_price = None
        self.maximum_price = None
        self.property_type = None
        self.date = str(datetime.today())

    def get_search_information(self) -> None:
        self.search_details = SearchDetails()
        self.city = self.search_details.city_query()
        self.minimum_price = self.search_details.min_price_query()
        self.maximum_price = self.search_details.max_price_query()
        self.property_type = self.search_details.property_type_query()

    def confirm_user_input(self) -> None:
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

            if confirmation == 'y':
                details_confirmation = True

            else:
                print('\nPlease enter the search details again.\n')

    def get_realtor_listings(self) -> str:
        driver = webdriver.Firefox()
        realtor_dot_com_scraper = RealtorDotComWebScraper(driver, self.city, self.minimum_price, self.maximum_price,
                                                          self.property_type)
        realtor_dot_com_scraper.open_webpage(self.date)
        listings = realtor_dot_com_scraper.get_listings()
        driver.close()
        return listings

    def get_trulia_listings(self) -> str:
        driver = webdriver.Firefox()
        trulia_scraper = TruliaWebScraper(driver, self.city, self.minimum_price, self.maximum_price,
                                          self.property_type)
        trulia_scraper.open_webpage(self.date)
        listings = trulia_scraper.get_listings()
        driver.close()
        return listings

    def get_homes_listings(self) -> str:
        driver = webdriver.Firefox()
        home_scraper = HomesDotComWebScraper(driver, self.city, self.minimum_price, self.maximum_price,
                                             self.property_type)
        home_scraper.open_webpage(self.date)
        listings = home_scraper.get_listings()
        driver.close()
        return listings

    def run_realtor_scraper(self) -> None:
        self.get_search_information()
        self.confirm_user_input()
        data = self.get_realtor_listings()
        self.data_formatter.format_realtor_dot_com_data(data, self.date)

    def run_trulia_scraper(self) -> None:
        self.get_search_information()
        self.confirm_user_input()
        data = self.get_trulia_listings()
        self.data_formatter.format_trulia_data(data, self.date)

    def run_homes_scraper(self) -> None:
        self.get_search_information()
        self.confirm_user_input()
        data = self.get_homes_listings()
        self.data_formatter.format_homes_dot_com_data(data, self.date)
