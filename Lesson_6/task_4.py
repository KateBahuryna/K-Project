from datetime import datetime
from time import sleep


def func_sleep():
    moment = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')   # время в данный момент
    sleep(1)                                                          # задержка в секунду
    return moment


def lst_time(n: int) -> list:
    time = [func_sleep() for _ in range(n)]                           # создание списка
    return time


number = int(input('Введите число n '))
print(lst_time(number))
