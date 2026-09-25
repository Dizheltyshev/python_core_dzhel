# 2. Напишите программу авторизации пользователя

password = "Python123"
attempts = 0

while attempts < 3:
    user_password = input("Введите пароль: ")

    if user_password == password:
        print("Авторизация пройдена!")
        break
    else:
        attempts += 1
        print("Неправильный пароль.")

if attempts == 3:
    print("Неправильный пароль. Доступ запрещен.")