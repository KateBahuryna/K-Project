x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))

if x > 10 and y > 10:
    print('Оба числа больше 10')

elif x > 10 or y > 10:
    print('Одно из чисел больше 10')

else:
    print('Отработала секция else')
