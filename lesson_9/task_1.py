
first_dict = {'a': 1, 'b': 2, 'c': 3}
second_dict = {'c': 3, 'd': 4, 'e': 5}

for key2, value2 in second_dict.items():
    if first_dict.get(key2):
        first_dict[key2] = [first_dict[key2], value2]
    else:
        first_dict[key2] = [None, value2]

for key1, value1 in first_dict.items():
    if not second_dict.get(key1):
        first_dict[key1] = [value1, None]

merged_dict = first_dict
print(merged_dict)
