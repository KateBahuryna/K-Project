b1 = b'bytes'       # создание байтов
print(b1, type(b1))

print('Байты'.encode('utf-8'))          # создание байтов

a = bytes('bytes', encoding = 'utf-8')            # создание байтов
print(a)

b = bytes([50, 100, 125, 140])                         # создание байтов
print(b)

x1 = chr(50)
print(x1)

x3 = b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'.decode('utf-8')     # преобразование в строку
print(x3)




