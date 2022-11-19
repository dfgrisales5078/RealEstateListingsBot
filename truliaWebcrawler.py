from selenium.webdriver.common.by import By
from webcrawlerPrototype import WebcrawlerPrototype


class TruliaWebcrawler(WebcrawlerPrototype):
    def __init__(self, driver, city, minimum_price, maximum_price, property_type):
        super().__init__(driver, city, minimum_price, maximum_price, property_type)

    def open_webpage(self, date):
        self.driver.get(self.get_formatted_url())
        self.driver.save_screenshot("trulia-screenshot.png")
        assert "Page not found" not in self.driver.page_source

    def close_webpage(self):
        self.driver.close()

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

    def get_listings(self) -> str:
        listings = self.driver.find_element(
            By.XPATH, '//*[@id="resultsColumn"]/div[1]/ul')

        print(listings.text)
        return listings.text
