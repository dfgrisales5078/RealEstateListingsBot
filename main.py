from selenium import webdriver
from truliaBot import TruliaBot
from realtorDotComBot import RealtorDotComBot
from searchDetails import SearchDetails

if __name__ == '__main__':
    search_details = SearchDetails()
    city = search_details.set_city()
    minimum_price = search_details.set_min_price()
    maximum_price = search_details.set_max_price()
    property_type = search_details.set_property_type()

    details_confirmation = False
    while not details_confirmation:
        print("Please enter the following details to search for properties: ")

        confirmation = input(f'\nPlease confirm the details of your search:\n'
                             f'City: {city}\n'
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

    driver = webdriver.Firefox()
    # realtor_dot_com_bot = RealtorDotComBot(driver, city, minimum_price, maximum_price, property_type)
    # realtor_dot_com_bot.open_webpage()

    trulia_bot = TruliaBot(driver, city, minimum_price, maximum_price, property_type)
    trulia_bot.open_webpage()
