from selenium import webdriver
from time import sleep
from zillowBot import ZillowBot
import searchDetails


if __name__ == '__main__':
    driver = webdriver.Chrome()
    zillow = ZillowBot(driver)
    zillow.open_webpage('https://www.zillow.com')
    sleep(15)
    zillow.close_webpage()

    # search_details = searchDetails()
    # city = search_details.set_city()

    # city =
    # min_price=
    # max_price=
    # property_type =
