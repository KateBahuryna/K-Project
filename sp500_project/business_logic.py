import random
from statistics import mean
from data_access import (get_all_records, write_in_database,
                         change_info_in_database)
from random import randint
from string import (ascii_letters, ascii_uppercase)
from time import time

decorator_cache = {}


def cache(cache_time=10):
    def inner(func):
        def wrapper(*args, **kwargs):
            value, expiration_time = decorator_cache.get(args, (None, None))
            print(f'Cache_storage: {decorator_cache}')
            if value and time() <= expiration_time:
                print('from cache')
                return value

            print('without cache')
            res = func(*args, **kwargs)
            expiration_time = time() + cache_time
            decorator_cache[args] = (res, expiration_time)
            return res
        return wrapper
    return inner


@cache(cache_time=10)
def find_info_by_name(company_name):
    database = get_all_records()
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


@cache(cache_time=5)
def get_all_companies_by_sector(sector_name):
    database = get_all_records()
    result = []
    for row in database:
        if sector_name.lower() in row.get('Sector').lower():
            result.append(row.get('Name'))
    return result


def calculate_average_price():
    database = get_all_records()
    result = []
    for row in database:
        result.append(float(row.get('Price')))
    result_average = mean(result)
    return result_average


def get_top10_companies():
    database = get_all_records()
    result = []
    for row in database:
        result.append((row.get('Name'), float(row.get('Price'))))
    result_sorted = sorted(result, key=lambda price: price[1],
                           reverse=True)[:10]
    return result_sorted


def check_symbol_in_database(symbol):
    database = get_all_records()
    flag = False
    for row in database:
        if symbol.lower() == row.get('Symbol').lower():
            flag = True
            break
    return flag


def check_name_in_database(name):
    database = get_all_records()
    flag = False
    for row in database:
        if name.lower() == row.get('Name').lower():
            flag = True
            break
    return flag


def check_sector_in_database(sector):
    database = get_all_records()
    flag = False
    for row in database:
        if sector.lower() == row.get('Sector').lower():
            flag = True
            break
    return flag


def add_new_company(symbol, name, sector, price):
    new_string_dict = {"Symbol": symbol,
                       "Name": name,
                       "Sector": sector,
                       "Price": price}
    return write_in_database(new_string_dict)


def update_company_name(symbol, new_name):
    database = get_all_records()
    for row in database:
        if symbol.lower() == row.get('Symbol').lower():
            row['Name'] = new_name
    return change_info_in_database(database)


def delete_company(symbol):
    database = get_all_records()
    for row in database:
        if symbol.lower() == row.get('Symbol').lower():
            index = database.index(row)
            del database[index]
    return change_info_in_database(database)


def truncate_all():
    file = []
    return change_info_in_database(file)


def populate_file_with_random_data(number):
    new_database = []
    for i in range(int(number)):
        new_database.append({"Symbol": ''.join(random.sample
                                               (ascii_uppercase, 3)),
                            "Name": ''.join(random.sample
                                            (ascii_letters, 6)),
                             "Sector": ''.join(random.sample
                                               (ascii_letters, 8)),
                             "Price": randint(0, 1000)})
    return change_info_in_database(new_database)
