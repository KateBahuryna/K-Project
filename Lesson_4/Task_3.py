# # из НЕизменяемых типов в изменяемые
# str_1 = '5'
# str_2 = '5'
# str_3 = '5'
#
# print('Одинаковые идентификаторы: ', id(str_1), id(str_2), id(str_3), sep='\n')
#
# str_1x = list(str_1)
# str_2x = list(str_2)
# str_3x = list(str_3)
#
# print('Разные идентификаторы: ', id(str_1x), id(str_2x), id(str_3x), sep='\n')
import sys

# из изменяемых типов в НЕизменяемые. Интернирование

set_1 = {'5', 3,  12.5}
set_2 = {'5', 3,  12.5}

print('Set: ', id(set_1), id(set_2), sep='\n')
print(type(set_1), type(set_2))

set_1x = str(set_1)
set_2x = str(set_1)

y = sys.intern(set_1x)
z = sys.intern(set_2x)

print('Set: ', id(y), id(z), sep='\n')
print(type(y), type(z))
