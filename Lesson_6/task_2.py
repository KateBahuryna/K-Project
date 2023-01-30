def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)


n = int(input('Введите число n '))
factorial_recursive(n)
print(f'Факториал {n} это {factorial_recursive(n)}')
