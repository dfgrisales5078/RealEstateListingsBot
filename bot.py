class Bot:
    def __init__(self, driver, city_or_zipcode, minimum_price, maximum_price, property_type):
        self.driver = driver
        self.city_or_zipcode = city_or_zipcode
        self.minimum_price = minimum_price
        self.maximum_price = maximum_price
        self.property_type = property_type
        self.url = None

    def open_webpage(self, url):
        self.driver.get(url)
        assert "Page not found" not in self.driver.page_source

    def close_webpage(self):
        self.driver.close()

    def set_city_or_zipcode(self):
        pass

    def set_property_type(self):
        pass

    def set_price_ranges(self):
        pass

    def get_listings(self):
        pass
