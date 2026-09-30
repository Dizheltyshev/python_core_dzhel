# Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.
with open("numbers.txt", "r") as file:
    numbers = file.read().split()

squares = list(map(lambda x: float(x) ** 2, numbers))

with open("numbers.txt", "w") as file:
    for square in squares:
        file.write(f"{square}\n")