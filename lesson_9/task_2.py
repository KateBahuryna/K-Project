# ЗАДАНИЕ 3

letter = input('Введите букву: ')

if letter.islower():
    letter2 = letter.upper()
else:
    letter2 = letter.lower()

count = 0
with open('text_task2.TXT') as file:
    for line in file:
        count += line.count(letter) + line.count(letter2)

print(count)
