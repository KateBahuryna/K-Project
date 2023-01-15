# integer
# a = 7
# print(type(a))
# b = 2
# print(-b)   # смена знака
#
# c, d = 3, 10
# print(c, d)
# d, c = c, d # замена значений
# print(c, d)
#
# e = abs(-30) # модуль числа
# print(e)
#
# f = divmod(5, 8) #(x//y, x%y)
# print(f)
#
# k = pow(3, 2) # возведение в степень, 2 способ
# print(k)


# float
# d = 12.5
# print(type(d))
# e = 34.1
# x = abs(d - e)   # модуль
# print(x)
#
# y = round(x)     # математическое округление
# print(y)

# bool
# y = False
# print(type(y))
#
# x = 6 > 8
# print(x)
#
# z = 6 != 8
# print(z)
#
# k = 0
# print(bool(k))
#
# l = 1
# print(bool(l))
#
# m = -5
# print(bool(m))

# string - неизменяемый тип данных
x = 'Hello'
print(type(x))
print(x[0])    # доступ к индексу
print(x[-1])    # доступ по отрицательному индексу

y = 'world'
z = x+y    # сложение строк
print(z)

print('world' * 3)     # дублирование строки

print(len('world'))    # определение длины строки

c = 'Happy Pythoning!'    # извлечение части строки
print(c[1:7])
print(c[1:7:2])           # извлечение части строки с шагом
print(c.lower())          # написание с маленькой буквы
print(c.upper())          # написание с заглавной буквы
print(c.find('p'))   # находит первое значение в строке и возвращает ее индекс
print(c.replace('p', 'w'))     # замена значений в строке
