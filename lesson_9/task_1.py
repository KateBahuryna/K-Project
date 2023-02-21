
first_dict = {'a': 1, 'b': 2, 'c': 3}
second_dict = {'c': 3, 'd': 4, 'e': 5}

list1 = list(first_dict.keys())
list2 = list(second_dict.keys())
list_joined = set(list1 + list2)
print(list_joined)

result = {}
for key in list_joined:
    if first_dict.get(key):
        first = first_dict[key]
    else:
        first = None
    if second_dict.get(key):
        second = second_dict[key]
    else:
        second = None
    result[key] = [first, second]
print(result)
