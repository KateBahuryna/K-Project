def invert(x):
    dict2 = dict(zip(x.values(), x.keys()))   # замена ключей и значений
    print(dict2)


dct1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}    # исходный словарь
print(dct1)
invert(dct1)
