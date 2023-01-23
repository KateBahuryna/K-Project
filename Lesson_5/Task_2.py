# задание 2
# name_age = input('Введите имя пользователя и возраст ')
# name_age_s = name_age.split()
# name, age0 = name_age_s[0], name_age_s[1]
#
# if age0.isdigit() == True:  # проверяет, что введено число, а не какой-либо другой символ
#     age = int(age0)
#     if age == 0:
#         print('Ошибка, повторите ввод')
#     elif age < 10:
#         print(f'Привет, шкет {name}')
#     elif 10 <= age <= 18:
#         print(f'Как жизнь, {name}?')
#     elif 18 < age <= 100:
#         print(f'Что желаете, {name}?')
#     else:
#         print(f'{name}, вы лжете - в наше время столько не живут...')
# else:
#     print('Ошибка, повторите ввод')


# задание 3 (вечный цикл)
name_age = input('Введите имя пользователя и возраст ')
name_age_s = name_age.split()
name, age0 = name_age_s[0], name_age_s[1]

while age0.isdigit() == True:  # проверяет, что введено число, а не какой-либо другой символ
    age = int(age0)
    if age == 0:
        print('Ошибка, повторите ввод')
        break
    elif age < 10:
        print(f'Привет, шкет {name}')
        break
    elif 10 <= age <= 18:
        print(f'Как жизнь, {name}?')
        break
    elif 18 < age <= 100:
        print(f'Что желаете, {name}?')
        break
    else:
        print(f'{name}, вы лжете - в наше время столько не живут...')
        break

if age0.isdigit() != True:
    print('Ошибка, повторите ввод')
