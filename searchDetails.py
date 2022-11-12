

class SearchDetails:
    def __init__(self, city, min_price, max_price, property_type='any'):
        self.search_query = {
            'city': '',
            'min_price': '',
            'max_price': '',
            'property_type': 'any'
        }

    def set_city(self):
        self.search_query['city'] = input(
            'Please enter the city for your search: ')
        return self.search_query['city']

    def set_min_price(self):
        self.search_query['min_price'] = input(
            'Please enter the minimum price to search: ')
        return self.search_query['min_price']

    def set_max_price(self):
        while True:
            self.search_query['max_price'] = input(
                'Please enter the minimum price to search: ')
            if self.search_query['max_price'] > self.search_query['min_price']:
                break
            else:
                print('Maximum price must be higher than minimum price. \n')
        return self.search_query['max_price']

    def set_property_type(self):
        self.search_query['property_type'] = input('Please enter the type of property to search (Apartment, '
                                                   'Townhome, House, or Any): ')
        return self.search_query['property_type']
