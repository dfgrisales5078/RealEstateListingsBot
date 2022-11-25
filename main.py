from facade import Facade


if __name__ == '__main__':
    while True:
        search_decision = input('Please make a selection (enter 1, 2 or 3): '
                                '\n1 to search realtor.com '
                                '\n2 to search trulia.com '
                                '\n3 to search homes.com\n')

        if search_decision == '1':
            realtor_listings = Facade()
            realtor_listings.run_realtor_bot()
            break

        elif search_decision == '2':
            trulia_listings = Facade()
            trulia_listings.run_trulia_bot()
            break

        elif search_decision == '3':
            trulia_listings = Facade()
            trulia_listings.run_homes_bot()
            break

        else:
            print("Invalid input. Please Try again \n")
