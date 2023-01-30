"""Вывести слова-полиндромы из кортежа"""
words = ('казак', 'мама', 'шалаш', 'кефир', 'нога', 'заказ')

result = tuple(filter(lambda x: x == x[::-1], words))

print(result)
