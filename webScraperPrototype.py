from abc import ABC, abstractmethod


class WebScraperPrototype(ABC):
    def __init__(self, driver, city, minimum_price, maximum_price, property_type):
        self.driver = driver
        self.city = city
        self.minimum_price = minimum_price
        self.maximum_price = maximum_price
        self.property_type = property_type
        self.url = None

    @abstractmethod
    def open_webpage(self, date) -> None:
        pass

    @abstractmethod
    def close_webpage(self) -> None:
        pass

    @abstractmethod
    def set_property_type(self) -> None:
        pass

    @abstractmethod
    def get_formatted_url(self) -> None:
        pass

    @abstractmethod
    def get_listings(self) -> None:
        pass
