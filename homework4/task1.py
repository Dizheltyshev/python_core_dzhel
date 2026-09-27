# Вывести первый, второй, предпоследний и последний элементы данного файла
with open("numbers.txt", "r") as file:
    numbers = file.read().split()

if len(numbers) < 3:
    print("Ошибка: в файле меньше 3 чисел")
else:
    print(numbers[0])
    print(numbers[1])
    print(numbers[-2])
    print(numbers[-1])