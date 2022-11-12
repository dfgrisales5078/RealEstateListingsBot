from bot import Bot
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ZillowBot(Bot):
    def __init__(self, driver):
        super().__init__(driver)

    def open_webpage(self, url):
        self.driver.get(url)

    def close_webpage(self):
        pass
