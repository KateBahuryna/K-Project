def number_check(str1):
    """Проверка, что введенное значение является числом"""
    num_clean1 = str1.replace('-', '', 1)  # удаление минуса из строки
    num_clean = num_clean1.replace('.', '', 1)  # удаление точки из строки
    if not num_clean.isdigit():  # проверка с помощью isdigit
        check1 = False
        print(f'Вы ввели некорректное число: {str1}')  # сообщение об ошибке
    else:
        check1 = True
    return check1


def work(x):
    """Работа с самим числом"""
    num_work = float(x)  # изменение типа на float
    num_int = int(num_work)  # изменение типа на integer
    if num_work < 0 and num_work % num_int != 0:
        print(f'Вы ввели отрицательное дробное число: {num_work}')
    elif num_work < 0 and num_work % num_int == 0:
        print(f'Вы ввели отрицательное целое число: {num_work}')
    elif num_work > 0 and num_work % num_int != 0:
        print(f'Вы ввели положительное дробное число: {num_work}')
    elif num_work > 0 and num_work % num_int == 0:
        print(f'Вы ввели положительное целое число: {num_work}')
    else:
        print('Ваше число "ноль"')


string = input('Введите число ')

check = number_check(string)  # запуск первой функции

if check:
    work(string)      # запуск второй функции
