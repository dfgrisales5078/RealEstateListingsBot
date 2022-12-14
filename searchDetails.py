class SearchDetails:
    def __init__(self):
        self.search_query = {
            'city': '',
            'min_price': 0,
            'max_price': 0,
            'property_type': 'any'
        }

    def city_query(self) -> str:
        self.search_query['city'] = input(
            'Enter the city (e.g.: Estero): ').lower()
        self.search_query['city'].replace(' ', '-')
        return self.search_query['city']

    def min_price_query(self) -> int:
        self.search_query['min_price'] = int(input(
            'Enter the minimum price (e.g.: 400,000): '))
        return self.search_query['min_price']

    def max_price_query(self) -> int:
        while True:
            self.search_query['max_price'] = int(input(
                'Enter the maximum price (e.g.: 1,000,000): '))
            if self.search_query['max_price'] > self.search_query['min_price']:
                break
            else:
                print('Maximum price must be higher than minimum price. \n')
        return self.search_query['max_price']

    def property_type_query(self) -> str:
        property_types = ['apartment', 'townhome', 'house', 'any']

        while True:
            self.search_query['property_type'] = input('Please enter the type of property to search (Apartment, '
                                                       'Townhome, House, or Any): ').lower()

            if self.search_query['property_type'] in property_types:
                return self.search_query['property_type']
            else:
                print('Invalid property type entered, please try again. ')
