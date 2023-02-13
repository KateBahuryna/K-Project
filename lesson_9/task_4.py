# ЗАДАНИЕ
# Создать программу с консольным интерфейсом, с помощью которой
# пользователь смог бы просматривать котировки акций компаний из
# рейтинга sp500: производить поиск по базе компаний, выводить рейтинг,
# получать среднюю стоимость котировок.

# import csv


# def find_info_by_name(name):    # TODO FUNCTION 1
#     with open('sp500.csv', 'r') as file:
#         database = csv.DictReader(file)
#
#
# def get_all_companies_by_sector(sector):   # TODO FUNCTION 2
#     with open('sp500.csv', 'r') as file:
#         database = csv.DictReader(file)


# def calculate_average_price():    # TODO FUNCTION 3
#     with open('sp500.csv', 'r') as file:
#         database = csv.DictReader(file)

#
# def get_top10_companies():      # TODO FUNCTION 4
#     with open('sp500.csv', 'r') as file:
#         database = csv.DictReader(file)
#         top10 = sorted(database, key=lambda x: float(x['Price']),
#         reverse=True)[:10]
#     return top10


choice = int(input("""
Choose the action from the menu:
1 - Find info by name
2 - Get all companies by sector
3 - Calculate average price
4 - Get top 10 companies
5 - Exit
Your choice: """))

# if choice == 1:
#     company_name = input('Input company name: ')
#     print(find_info_by_name(company_name))
#
# if choice == 2:
#     sector_name = input('Input sector name: ')
#     print(get_all_companies_by_sector(sector_name))

# if choice == 3:
#     print(calculate_average_price())
#
# if choice == 4:
#     print(get_top10_companies())

# if choice == 5:
#     print('GOODBYE!')
