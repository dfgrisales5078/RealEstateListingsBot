class Bot:
    def __init__(self, driver, city, minimum_price, maximum_price, property_type):
        self.driver = driver
        self.city = city
        self.minimum_price = minimum_price
        self.maximum_price = maximum_price
        self.property_type = property_type
        self.url = None

    def open_webpage(self):
        self.driver.get(self.get_formatted_url())
        assert "Page not found" not in self.driver.page_source

    def close_webpage(self):
        self.driver.close()

    def set_property_type(self):
        pass

    def get_formatted_url(self):
        pass

    def get_listings(self):
        pass
