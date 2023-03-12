import csv


def get_all_records():
    with open('sp500.csv', 'r') as file:
        return list(csv.DictReader(file))


def write_in_database(new_string):
    with open('sp500.csv', 'a') as file:
        fieldnames = ["Symbol", "Name", "Sector", "Price"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(new_string)


def change_info_in_database(new_database):
    with open('sp500.csv', 'w+') as file:
        fieldnames = ["Symbol", "Name", "Sector", "Price", "Price/Earnings",
                      "Dividend Yield", "Earnings/Share", "52 Week Low",
                      "52 Week High", "Market Cap", "EBITDA", "Price/Sales",
                      "Price/Book", "SEC Filings"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_database)
