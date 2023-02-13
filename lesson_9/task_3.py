# ЗАДАНИЕ 4
# Написать функцию, которая принимает n-ое количество координат точек.
# И в ответ возвращает длину маршрута между ними.
# Каждая координата представлена кортежем, состоящим из двух объектов типа int.
# Длина отрезка: https://www.calc.ru/Formula-Dliny-Otrezka.html
# Примеры использования функции:
# result = distance((1, 1), (1, 2), (3, 3))
# print(result) # выведет 1
#
# В общем виде:
# result = distance((1, 1), (2, 3), (5, 8), ..., (xn, yn))

def calculate_route(coord: tuple) -> int:
    distance = 0
    for index, point in enumerate(coord):
        if index == len(coord)-1:
            break
        x1, y1 = point
        x2, y2 = coord[index+1]
        distance += ((x2-x1) ** 2 + (y2-y1)) ** 0.5
    return distance


points = ((1, 1), (2, 3), (4, 5))
print(calculate_route(points))
