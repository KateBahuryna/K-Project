from business_logic import (find_info_by_name, get_all_companies_by_sector,
                            calculate_average_price, get_top10_companies,
                            check_name_in_database, check_sector_in_database,
                            check_symbol_in_database, add_new_company,
                            update_company_name, delete_company,
                            truncate_all, populate_file_with_random_data)
from validators import (validate_user_choice, validate_new_company_symbol,
                        validate_new_company_name, validate_new_company_price,
                        validate_number_for_generation)
from errors import (WrongCompanyName, WrongCompanySymbol,
                    WrongUserInputError, WrongPriceError,
                    WrongNumberForGeneration, DatabaseIssue)


while True:
    choice = input("Choose the action from the menu:\n"
                   "1 - Find info by name\n"
                   "2 - Get all companies by sector\n"
                   "3 - Calculate average price\n"
                   "4 - Get top 10 companies\n"
                   "5 - Add new company\n"
                   "6 - Update company name\n"
                   "7 - Delete company\n"
                   "8 - Truncate all\n"
                   "9 - Populate file with random data\n"
                   "10 - Exit\n"
                   "Your choice: ")
    try:
        validate_user_choice(choice)
    except WrongUserInputError as err:
        print(err)
        continue
    if choice == "10":
        print('GOODBYE!')
        break

    elif choice == "1":
        company_name = input('Input company name: ')
        result_choice1 = find_info_by_name(company_name)
        print(result_choice1)

    elif choice == "2":
        sector_name = input('Input sector name: ')
        result_choice2 = get_all_companies_by_sector(sector_name)
        print(result_choice2)

    elif choice == "3":
        result_choice3 = calculate_average_price()
        print(result_choice3)

    elif choice == "4":
        result_choice4 = get_top10_companies()
        print(result_choice4)

    elif choice == "5":

        while True:
            symbol_choice5 = input('Input symbol: ')
            name_choice5 = input('Input company name: ')
            sector_choice5 = input('Input sector name: ')
            price_choice5 = input('Input price: ')
            try:
                validate_new_company_symbol(symbol_choice5)
                validate_new_company_name(name_choice5)
                validate_new_company_price(price_choice5)
                break
            except (WrongCompanySymbol, WrongCompanyName,
                    WrongPriceError) as err:
                print(err)

        available_symbol = check_symbol_in_database(symbol_choice5)
        available_name = check_name_in_database(name_choice5)
        available_sector = check_sector_in_database(sector_choice5)

        if not (available_symbol and
                available_name) and available_sector:
            add_new_company(symbol_choice5, name_choice5,
                            sector_choice5, price_choice5)
        else:
            raise DatabaseIssue("ERROR. The company has already existed "
                                "or this sector isn't")

    elif choice == "6":

        while True:
            symbol_choice6 = input('Input symbol: ')
            name_choice6 = input('Input company name: ')
            try:
                validate_new_company_name(name_choice6)
                break
            except WrongCompanyName as err:
                print(err)

        if check_symbol_in_database(symbol_choice6):
            update_company_name(symbol_choice6, name_choice6)

        else:
            raise DatabaseIssue("ERROR. This symbol doesn't exist in database")

    elif choice == "7":

        symbol_choice7 = input('Input symbol: ')
        if check_symbol_in_database(symbol_choice7):
            delete_company(symbol_choice7)

        else:
            raise DatabaseIssue("ERROR. This symbol doesn't exist in database")

    elif choice == "8":

        truncate_all()

    elif choice == "9":

        while True:
            number_choice9 = input('Input number for generation: ')
            try:
                validate_number_for_generation(number_choice9)
                break
            except WrongNumberForGeneration as err:
                print(err)

        populate_file_with_random_data(number_choice9)
