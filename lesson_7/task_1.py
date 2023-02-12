"""Определение четности числа с помощью lambda"""
check = lambda x: 'Число четное' if x % 2 == 0 else 'Число нечетное'

numb = int(input('Введите любое число '))
print(check(numb))
