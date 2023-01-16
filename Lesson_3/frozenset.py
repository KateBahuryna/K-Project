# frozenset - неизменяемоеб хешируемое множество
a = set('Hello Python!')
print(type(a))
b = frozenset('Hello Python!')  # создание frozenset
print(type(b))

print(a == b)

b1 = frozenset('Hello Pythonnnnn!')
print(a == b1)

print(a-b)    # Error