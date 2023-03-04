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
    with open('sp500.csv', 'r') as file:
        headlines = csv.DictReader(file).fieldnames
    with open('sp500.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=headlines)
        writer.writeheader()
        writer.writerows(new_database)
