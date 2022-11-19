class DataFormatter:
    @staticmethod
    def format_trulia_data(data, date):
        with open('data.txt', 'w') as data_file:
            data_file.write(data)

        with open(f'trulia-listings-{date[:10]}.txt', 'w') as listings_file:
            with open('data.txt', 'r+') as data_file:
                for line in data_file.readlines():
                    if line.startswith('NEW'):
                        continue
                    if line.startswith('$'):
                        listings_file.write('\n')
                        listings_file.write(line)
                    else:
                        listings_file.write(line)

    @staticmethod
    def format_realtor_dot_com_data(data, date):
        with open('data.txt', 'w') as data_file:
            data_file.write(data)

        with open(f'realtor-listings-{date[:10]}.txt', 'w') as listings_file:
            with open('data.txt', 'r+') as data_file:
                for line in data_file.readlines():
                    if line.startswith('NEW') or line.startswith('Brokered') or line.startswith('Email'):
                        continue
                    if line.startswith('For') or line.startswith('Pending') or line.startswith('Contingent'):
                        listings_file.write('\n')
                        listings_file.write(line)
                    else:
                        listings_file.write(line)

                    if line.startswith('Previous'):
                        break
