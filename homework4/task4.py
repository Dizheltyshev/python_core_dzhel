# Даны два файла произвольного типа. Поменять местами их содержимое.
# Файлы должны быть бинарного типа.
with open("binary1", "rb") as b1:
    data1 = b1.read()

with open("binary2", "rb") as b2:
    data2 = b2.read()

with open("binary1", "wb") as b1:
    b1.write(data2)

with open("binary2", "wb") as b2:
    b2.write(data1)