# изменяемые типы данных list, set, dict. Разные идентификаторы
list_1 = ['5', 3, [1, 5, 7], 12.5]
list_2 = ['5', 3, [1, 5, 7], 12.5]

print('List: ', id(list_1), id(list_2), sep='\n')
print(type(list_1), type(list_2))

set_1 = {'5', 3,  12.5}
set_2 = {'5', 3,  12.5}

print('Set: ', id(set_1), id(set_2), sep='\n')
print(type(set_1), type(set_2))

dict_1 = dict(one=1, two=2, three=3)
dict_2 = dict(one=1, two=2, three=3)

print('Dict: ', id(dict_1), id(dict_2), sep='\n')
print(type(dict_1), type(dict_2))
