import random
number = random.randint(1, 100)
print(number)    # проверка рандомного числа

guess = int(input('Угадайте число от 0 до 100 '))
count = 1
while guess != number:
    count += 1
    if guess < number:
        guess = int(input('Попробуйте число побольше '))
    else:
        guess = int(input('Попробуйте число поменьше '))
print(f'Вам понадобилось {count} попыток ')
