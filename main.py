from facade import Facade

if __name__ == '__main__':
    search_decision = int(input('Enter 1 to search realtor.com or 2 to search trulia.com: '))

    if search_decision == 1:
        realtor_listings = Facade()
        realtor_data = realtor_listings.run_realtor_bot()
        print('\nPrint from main\n', realtor_data)

    elif search_decision == 2:
        trulia_listings = Facade()
        trulia_data = trulia_listings.run_trulia_bot()
        print('\nPrint from main\n', trulia_data)
