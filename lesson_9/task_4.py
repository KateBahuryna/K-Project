# ЗАДАНИЕ
# Создать программу с консольным интерфейсом, с помощью которой
# пользователь смог бы просматривать котировки акций компаний из
# рейтинга sp500: производить поиск по базе компаний, выводить рейтинг,
# получать среднюю стоимость котировок.
# +декоратор кэширования

import csv
from statistics import mean


def decorator(func):
    decorator_cache = {}

    def wrapper(*args, **kwargs):
        if 'result' not in decorator_cache:
            decorator_cache['result'] = func(*args, **kwargs)
            print('result saved')
        else:
            print('already in memory')
        return decorator_cache['result']
    return wrapper


@decorator
def find_info_by_name(company_name):
    with open('sp500.csv', 'r') as file:
        database = csv.DictReader(file)
        result = []
        for row in database:
            if company_name.lower() in row.get('Name').lower():
                result.append({
                    'Symbol': row.get('Symbol'),
                    'Name': row.get('Name'),
                    'Sector': row.get('Sector'),
                    'Stock price': row.get('Price')
                    }
                )
        return result


@decorator
def get_all_companies_by_sector(sector_name):
    with open('sp500.csv', 'r') as file:
        database = csv.DictReader(file)
        result = []
        for row in database:
            if sector_name.lower() in row.get('Sector').lower():
                result.append(row.get('Name'))
        return result


@decorator
def calculate_average_price():
    with open('sp500.csv', 'r') as file:
        database = csv.DictReader(file)
        result = []
        for row in database:
            result.append(float(row.get('Price')))
        result_average = mean(result)
        return result_average


@decorator
def get_top10_companies():
    with open('sp500.csv', 'r') as file:
        database = csv.DictReader(file)
        result = []
        for row in database:
            result.append((row.get('Name'),
                           float(row.get('Price'))))
        result_sorted = sorted(result, key=lambda price: price[1],
                               reverse=True)[:10]
        return result_sorted


while True:
    choice = int(input("Choose the action from the menu:\n"
                       "1 - Find info by name\n"
                       "2 - Get all companies by sector\n"
                       "3 - Calculate average price\n"
                       "4 - Get top 10 companies\n"
                       "5 - Exit\n"
                       "Your choice: "))
    if choice == 5:
        print('GOODBYE!')
        break

    elif choice == 1:
        company_name = input('Input company name: ')
        result_choice1 = find_info_by_name(company_name=company_name)
        print(result_choice1)

    elif choice == 2:
        sector_name = input('Input sector name: ')
        result_choice2 = get_all_companies_by_sector(sector_name=sector_name)
        print(result_choice2)

    elif choice == 3:
        result_choice3 = calculate_average_price()
        print(result_choice3)

    elif choice == 4:
        result_choice4 = get_top10_companies()
        print(result_choice4)

    else:
        print('ERROR')
