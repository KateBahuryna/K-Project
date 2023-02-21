import json
import csv
from random import randint


with open('file_json.json', 'r') as file2:  # открытие на чтение файла json
    data = json.load(file2)         # выгрузка из файла json
    data_lst = [[k, *v] for k, v in data.items()]  # преобразование словаря в list

print(data_lst)            # для проверки промежуточного результата

for item in data_lst:             # цикл для добавления номера телефона
    item.append(randint(375290000000, 375299999999))

print(data_lst)            # для проверки промежуточного результата


with open('file_csv.csv', 'w', encoding='utf-8') as file3:     # создание нового файла в формате csv
    fieldnames = ['ID', 'Name', 'Age', 'Phone number']      # добавление названия столбцов
    writer = csv.writer(file3)
    writer.writerow(fieldnames)  # запись названия столбцов в csv файл
    writer.writerows(data_lst)  # запись данных в csv файл построчно


