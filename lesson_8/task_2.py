str1 = input('Enter line №1... ')
str2 = input('Enter line №2... ')
str3 = input('Enter line №3... ')
str4 = input('Enter line №4... ')

with open('text2.txt', 'a') as t1:  # внесение 1 и 2 строки
    t1.write(str1 + '\n')
    t1.write(str2 + '\n')


with open('text2.txt', 'a+') as t1:  # внесение 3 и 4 строк
    t1.write(str3 + '\n')
    t1.write(str4)

with open('text2.txt', 'r') as t1:    # чтение файла
    read_file = t1.read()
    print(read_file)
