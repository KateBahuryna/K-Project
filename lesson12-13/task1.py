# ЗАДАНИЕ 1
# Создать класс Vectorа:
# (point_x1, point_y1) и (point_x2, point_y2)
# У класса реализовать метод
# length(self) - возвращает длину вектора (число)
# А также между объектами этого класса должны поддерживаться операции
# >, <, >=, <=, ==, !=
#
# Пример программы:
# v1 = Vector((0, 0), (0, 1))
# v2 = Vector((1, 1), (1, 2))
# v1 == v2 # True, так как одинаковая длина
# v3 = Vector((1, 1), (2, 2))
# v3 > v1 # True, так как длина v3 больше, чем длина v1

class Vector:
    def __init__(self, point1, point2):
        self.point1 = (point1[0], point1[1])
        self.point2 = (point2[0], point2[1])

    def __eq__(self, other):
        print('__eq__calls')
        return self.length == other.length

    def __ne__(self, other):
        print('__ne__calls')
        return self.length() != other.length()

    def __gt__(self, other):
        print('__gt__calls')
        return self.length() > other.length()

    def __ge__(self, other):
        print('__ge__calls')
        return self.length() >= other.length()

    def length(self):
        length = (((self.point2[0]-self.point1[0]) ** 2 +
                   (self.point2[1]-self.point1[1]) ** 2) ** 0.5)
        return length


v1 = Vector((7, 3), (0, 1))
v2 = Vector((0, 0), (0, 2))
print(v1.length())
print(v2.length())

print(v1 == v2)
print(v1 != v2)
print(v1 > v2)
print(v1 < v2)
print(v1 >= v2)
print(v1 <= v2)
