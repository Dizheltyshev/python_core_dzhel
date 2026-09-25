# 4. В программе хранится секретное число 37

secret = 37
attempts = 0
user_number = 0

while user_number != secret:
    user_number = int(input("Введите число: "))
    attempts += 1

    if user_number > secret:
        print("Ваше число больше")
    elif user_number < secret:
        print("Ваше число меньше")

print("Правильно!")
print(f"Количество попыток: {attempts}")