from facade import Facade

if __name__ == '__main__':
    while True:
        website_selection = input('Please make a website to search: '
                                  '\npress 1 to search realtor.com '
                                  '\npress 2 to search trulia.com '
                                  '\npress 3 to search homes.com\n'
                                  '\nor press enter to quit.\n')

        if website_selection == '':
            exit(0)

        facade = Facade()

        if website_selection == '1':
            facade.run_realtor_scraper()
            break

        elif website_selection == '2':
            facade.run_trulia_scraper()
            break

        elif website_selection == '3':
            facade.run_homes_scraper()
            break

        else:
            print("Invalid input. Please Try again \n")
