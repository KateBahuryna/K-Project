# # dict - неупорядоченные коллекции со входом по ключу
# d = {}          # cоздание пустого словаря
# print(type(d))
# d0 = dict()       # cоздание пустого словаря
# print(type(d0))
#
# d1 = {'yes':1, 'no':2}   # создание словаря. Способ1
# print(d1)
#
# d2 = dict(short='dict', long='dictionary')     # создание словаря. Способ2. В таком случае ключом может быть только строка
# print(d2)
#
#
# a = [['one',1], ['two', 2], ['three', 3]]     # создание словаря. Способ3. Через вложенный список
# d3 = dict(a)
# print(d3)
#
# d4 = dict.fromkeys(['one1', 'two2', 'three3'])   # создание словаря. Способ4.
# print(d4)
#
# d5 = dict.fromkeys(['one1', 'two2', 'three3'], 1000)    # создание словаря. Способ4.1.
# print(d5)

dict_main = {'yes': 1, 'no': 2, 800: 3}
print(dict_main)

print(dict_main[800])         # извлечение из словаря по ключу

dict_main['maybe'] = 3       # добавление пары (ключ+значение) в словарь
print(dict_main)

dict_main['maybe'] = 7       # изменение значения в словаре
print(dict_main)

del dict_main['yes']        # удаление ключа из словаря
print(dict_main)

print(len(dict_main))       # подсчет длины словаря

print(800 in dict_main)     # проверка, есть ли ключ в словаре. True/False

# dict_main.clear()            # удаление всего словаря
# print(dict_main)

print(dict_main.get(800))      # получение значения по ключу

print(dict_main.get(100, 'No such key'))      # Если отсутствует ключ, то выводит строку

# print(dict_main.setdefault(130))           # при обращении к несуществующему ключе, метод добавляет его в словарь
#

dict_main.pop('maybe')         # удаление пары по ключу
print(dict_main)

dict_main.popitem()            # удаление пары рандомно
print(dict_main)

print(dict_main.items())       # возвращает пары ключ-значение
