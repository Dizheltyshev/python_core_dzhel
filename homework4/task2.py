# Создать два новых файла, первый из которых содержит четные числа из исходного файла, а второй — нечетные
with open("numbers.txt", "r") as file:
    numbers = file.read().split()

with open("even.txt", "w") as even_file:
    for number in numbers:
        if int(number) % 2 == 0:
            even_file.write(number + "\n")

with open("odd.txt", "w") as odd_file:
    for number in numbers:
        if int(number) % 2 != 0:
            odd_file.write(number + "\n")