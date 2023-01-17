# tuple - неизменяемый тип данных, меньший размерб чем списков
a = [1, 2, 3, 4, 5]   # проверка размера
b = (1, 2, 3, 4, 5)
size_a = a.__sizeof__()
print(size_a)
size_b = b.__sizeof__()
print(size_b)


x = tuple()  # создание кортежа. Способ 1
print(type(x))

y = ('k', )  # создание кортежа. Способ 2
print(type(y))

z = tuple('Hello World!')
print(z)
print(z[3])   # запрос элемента кортежа по индексу

A = (2.5, ['a', True, 3.17], 8, 'False', 'L')    # вложенные кортежи
A1 = A[1]
A2 = A[1][1]
print(A2)

srez = A[1:3]   # срез кортежа (последний инжекс -1)
print(srez)

summa = A + z   # сложение кортежей
print(summa)

repeat = z * 3   # повторение кортежа
print(repeat)

n = repeat.count('l')  # считает количество элементов в кортеже
print(n)
