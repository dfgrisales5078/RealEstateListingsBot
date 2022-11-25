from webScraperPrototype import WebScraperPrototype
from selenium.webdriver.common.by import By


class HomesDotComWebScraper(WebScraperPrototype):
    def __init__(self, driver, city, minimum_price, maximum_price, property_type):
        super().__init__(driver, city, minimum_price, maximum_price, property_type)

    def open_webpage(self, date) -> None:
        self.driver.get(self.get_formatted_url())
        assert "Page not found" not in self.driver.page_source
        self.driver.save_screenshot("homes-screenshot.png")

    def close_webpage(self) -> None:
        self.driver.close()

    def set_property_type(self) -> str:
        if self.property_type == 'apartment':
            return 'condos-for-sale/'
        elif self.property_type == 'house':
            return 'houses-for-sale/'
        elif self.property_type == 'townhome':
            return 'townhouses-for-sale/'
        elif self.property_type == 'any':
            return 'any'

    def get_formatted_url(self) -> str:
        return f'https://www.homes.com/{self.city}-fl/{self.set_property_type()}?price-min={self.minimum_price}&price' \
               f'-max={self.maximum_price} '

    def get_listings(self) -> str:
        listings = self.driver.find_element(
            By.XPATH, '/html/body/main/section/section/div[2]/ul')

        print(listings.text)
        return listings.text
