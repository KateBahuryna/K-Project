import timeit


# print(timeit.timeit('x = 2 + 2'))
# print(timeit.timeit('x = sum([1, 5 ,7 ,100, 90])'))

code_to_test = """
a = range(100000)
b = [i*2 for i in a]
"""
elapsed_time = timeit. timeit(code_to_test, number=100)/100
print(elapsed_time)

code_to_test1 = """
a = range(100000)
b = []
for i in a:
    b.append(i*2)
"""
elapsed_time1 = timeit. timeit(code_to_test1, number=100)/100
print(elapsed_time1)
