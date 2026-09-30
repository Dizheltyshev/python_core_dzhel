import json

def load_users(users):
    try:
        with open(users, "r") as file:
            data = json.load(file)

        for user in data:
            try:
                login = user["login"]
                password = user["password"]
                status = user["status"]
            except KeyError as e:
                print(f"Ошибка: данные отсутствуют {e}")
                continue

            print(f"Login: {login}")
            print(f"Password: {password}")
            print(f"Expected result: {status}")
            print("-" * 24)

    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден - {e}")

    except json.JSONDecodeError as e:
        print(f"Ошибка: неправильный формат файла  - {e}")

    except Exception as e:
        print(f"Неизвестная ошибка: {e}")


load_users("users.json")