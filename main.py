from selenium import webdriver
from time import sleep
from zillowBot import ZillowBot
from searchDetails import SearchDetails

if __name__ == '__main__':

    details_confirmation = False
    while not details_confirmation:
        print("Please enter the following details to search for properties: ")
        search_details = SearchDetails()
        city_or_zipcode = search_details.set_city_or_zipcode()
        minimum_price = search_details.set_min_price()
        maximum_price = search_details.set_max_price()
        property_type = search_details.set_property_type()

        # ask_for_details_again = False
        # while not ask_for_details_again:
        confirmation = input(f'\nPlease confirm the details of your search:\n'
                             f'City or zipcode: {city_or_zipcode}\n'
                             f'Minimum price: {minimum_price}\n'
                             f'Maximum price: {maximum_price}\n'
                             f'Property type: {property_type}\n\n'
                             f'To confirm search details enter \'Y\', to re-enter the search information '
                             f'enter \'N\': ').lower()

        if confirmation != 'y':
            print('\nPlease enter the search details again.\n')

        else:
            details_confirmation = True
            break

    # driver = webdriver.Chrome()
    # zillow = ZillowBot(driver)
    # zillow.open_webpage('https://www.zillow.com')
    # sleep(15)
    # zillow.close_webpage()
