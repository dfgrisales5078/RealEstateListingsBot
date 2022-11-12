

class Bot:
    def __init__(self, driver):
        self.driver = driver
        self.url = None

    def open_webpage(self, url):
        self.driver.get(url)
        assert "Page not found" not in self.driver.page_source

    def close_webpage(self):
        self.driver.close()

    # def search_properties(self, city, home_type, max_price):
