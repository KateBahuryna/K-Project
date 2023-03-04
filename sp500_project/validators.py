from errors import (WrongPriceError, WrongUserInputError,
                    WrongCompanySymbol, WrongCompanyName,
                    WrongNumberForGeneration)


def validate_user_choice(choice):
    if not choice.isdigit():
        raise WrongUserInputError('ERROR: Choice must be a digit!')
    if not 1 <= int(choice) <= 11:
        raise WrongUserInputError('ERROR: Choice must be from 1 to 5!')


def validate_new_company_symbol(symbol_choice):
    if not 3 <= len(symbol_choice) <= 6:
        raise WrongCompanySymbol('ERROR: The company symbol must '
                                 'consist from 3 to 6 letters')
    for letter in symbol_choice:
        if not 65 <= ord(letter) <= 90:
            raise WrongCompanySymbol('ERROR: The company symbol must be'
                                     ' written in English and capitalised')


def validate_new_company_name(name_choice):
    if not 3 <= len(name_choice) <= 50:
        raise WrongCompanyName('ERROR: The company name must '
                               'consist from 3 to 50 letters')


def validate_new_company_price(price_choice):
    if '.' not in price_choice:
        raise WrongPriceError('The price should be float')
    if not 0 <= float(price_choice) <= 1000:
        raise WrongPriceError('ERROR: The price must be '
                              'in the range from 0 to 1000')


def validate_number_for_generation(number):
    if not 0 <= int(number) <= 10000:
        raise WrongNumberForGeneration('ERROR: The number must be '
                                       'in the range from 0 to 10000')
