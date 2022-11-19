from facade import Facade


if __name__ == '__main__':
    while True:
        search_decision = input('Enter 1 to search realtor.com or 2 to search trulia.com: ')

        if search_decision == '1':
            realtor_listings = Facade()
            realtor_listings.run_realtor_bot()
            break

        elif search_decision == '2':
            trulia_listings = Facade()
            trulia_listings.run_trulia_bot()
            break
        else:
            print("Invalid input. Please Try again \n")
