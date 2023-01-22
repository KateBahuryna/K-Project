name_age = input('Введите имя пользователя и возраст ')
name_age_s = name_age.split()
name, age = name_age_s[0], int(name_age_s[1])

if age <= 0 or type(age) != int:   # условие с int необязательно, так как ранее тип преобразовался
    print('Ошибка, повторите ввод')
elif age < 10:
    print(f'Привет, шкет {name}')
elif 10 <= age <= 18:
    print(f'Как жизнь, {name}?')
elif 18 < age <= 100:
    print(f'Что желаете, {name}?')
else:
    print(f'{name}, вы лжете - в наше время столько не живут...')
