# неизменяемые типы данных int, float, str, bool, tuple. Одинаковый идентификатор
str_1 = '5'
str_2 = '5'
str_3 = '5'

print('String: ', id(str_1), id(str_2), id(str_3), sep='\n')

int_1 = 7
int_2 = 7
int_3 = 7

print('Integer: ', id(int_1), id(int_2), id(int_3), sep='\n')

float_1 = 8.1
float_2 = 8.1
float_3 = 8.1

print('Float: ', id(float_1), id(float_2), id(float_3), sep='\n')

bool_1 = bool(3)
bool_2 = bool(3)
bool_3 = bool(3)

print('Bool: ', id(bool_1), id(bool_2), id(bool_3), sep='\n')
