"""Дан список чиселю Вернуть список строк с помощью map, lambda"""
numb = [1, 45, 78, 34, 5, 134, 7895]

string = list(map(lambda x: str(x), numb))
print(string, type(string[0]))
