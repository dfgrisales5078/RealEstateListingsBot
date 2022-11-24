from selenium.webdriver.common.by import By
from webScraperPrototype import WebScraperPrototype


class RealtorDotComWebScraper(WebScraperPrototype):
    def __init__(self, driver, city, minimum_price, maximum_price, property_type):
        super().__init__(driver, city, minimum_price, maximum_price, property_type)

    def open_webpage(self, date) -> None:
        self.driver.get(self.get_formatted_url())
        assert "Page not found" not in self.driver.page_source
        self.driver.save_screenshot("realtor-screenshot.png")

    def close_webpage(self) -> None:
        self.driver.close()

    def set_property_type(self) -> str:
        if self.property_type == 'apartment':
            return 'condo'
        elif self.property_type == 'house':
            return 'single-family-home'
        else:
            return self.property_type

    def get_formatted_url(self) -> str:
        return f'https://www.realtor.com/realestateandhomes-search/{self.city}_Fl/' \
               f'type-{self.set_property_type()}/price-{self.minimum_price}-{self.maximum_price}'

    def get_listings(self) -> str:
        listings = self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div[4]/section[1]')

        print(listings.text)
        return listings.text
