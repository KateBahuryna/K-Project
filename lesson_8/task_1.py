decod = b'r\xc3\xa9sum\xc3\xa9'.decode('utf-8')
print(decod, type(decod))

cod_latin = decod.encode('Latin1')
print(cod_latin)

decod_latin = cod_latin.decode('Latin1')
print(decod_latin, type(decod_latin))
