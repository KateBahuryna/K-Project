import time
from datetime import datetime


def decorator(func):
    """Определение времени выполнения функции"""
    def time_calc(*args, **kwargs):
        y = datetime.now()
        func(*args, **kwargs)
        t = datetime. now() - y
        print(f'Время выполения функции равно - {t}')
    return time_calc


@decorator                            # Функция №1
def numbers(x=4, y=6):
    z = x + y
    time.sleep(2)               # чтобы проверить правильность работы декоратора, так как функция выполняется быстро
    print(z)
    return z


numbers()


@decorator                              # Функция №2
def invert(x):
    dict2 = dict(zip(x.values(), x.keys()))
    time.sleep(6)
    print(dict2)
    return dict2


dict1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
invert(dict1)
