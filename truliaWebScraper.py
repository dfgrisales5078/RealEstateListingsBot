from selenium.webdriver.common.by import By
from webScraperPrototype import WebScraperPrototype


class TruliaWebScraper(WebScraperPrototype):
    def __init__(self, driver, city, minimum_price, maximum_price, property_type):
        super().__init__(driver, city, minimum_price, maximum_price, property_type)

    def open_webpage(self, date) -> None:
        self.driver.get(self.get_formatted_url())
        assert "Page not found" not in self.driver.page_source
        self.driver.save_screenshot("trulia-screenshot.png")

    def close_webpage(self) -> None:
        self.driver.close()

    def set_property_type(self) -> str:
        if self.property_type == 'apartment':
            return 'APARTMENT,CONDO,COOP'
        elif self.property_type == 'house':
            return 'SINGLE-FAMILY_HOME'
        elif self.property_type == 'townhome':
            return 'TOWNHOUSE'
        elif self.property_type == 'townhome':
            return 'ANY'

    def get_formatted_url(self) -> str:
        self.city.replace('-', '_')
        return f'https://www.trulia.com/for_sale/{self.city},FL/{self.minimum_price}-{self.maximum_price}_price' \
               f'/{self.set_property_type()}_type/ '

    def get_listings(self) -> str:
        listings = self.driver.find_element(
            By.XPATH, '//*[@id="resultsColumn"]/div[1]/ul')

        print(listings.text)
        return listings.text
