from selenium import webdriver
from time import sleep
from greaterFortMyersBot import GreaterFortMyersBot
from realtorDotComBot import RealtorDotComBot
from searchDetails import SearchDetails

if __name__ == '__main__':
    # search_details = SearchDetails()
    # city_or_zipcode = search_details.set_city_or_zipcode()
    # minimum_price = search_details.set_min_price()
    # maximum_price = search_details.set_max_price()
    # property_type = search_details.set_property_type()
    #
    # details_confirmation = False
    # while not details_confirmation:
    #     print("Please enter the following details to search for properties: ")
    #
    #     confirmation = input(f'\nPlease confirm the details of your search:\n'
    #                          f'City or zipcode: {city_or_zipcode}\n'
    #                          f'Minimum price: {minimum_price}\n'
    #                          f'Maximum price: {maximum_price}\n'
    #                          f'Property type: {property_type}\n\n'
    #                          f'To confirm search details enter \'Y\', to re-enter the search information '
    #                          f'enter \'N\': ').lower()
    #
    #     if confirmation != 'y':
    #         print('\nPlease enter the search details again.\n')
    #
    #     else:
    #         details_confirmation = True
    #         break

    city_or_zipcode = 'naples'
    minimum_price = 500000
    maximum_price = 850000
    property_type = 'house'

    driver = webdriver.Firefox()
    realtor_dot_com_bot = RealtorDotComBot(driver, city_or_zipcode, minimum_price, maximum_price, property_type)
    realtor_dot_com_bot.open_webpage('https://www.realtor.com')
    realtor_dot_com_bot.get_listings()

    # greater fort myers url:
    # realtor_dot_com_bot.open_webpage('https://www.greaterftmyers.com/property-search/search-form/')
