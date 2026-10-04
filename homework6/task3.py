# Напишите декоратор log_test, который перед запуском тестовой функции выводит её имя, после
# выполнения сообщает о завершении и выводит полученный результат.

import functools

def log_test(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Название теста: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Тест {func.__name__} завершён")
        print(f"Результат: {result}")
        return result

    return wrapper

@log_test
def authorisation(username, password):
    """Проверяет вход пользователя в систему."""
    if username == "user" and password == "qwerty1234":
        return "PASS"
    return "FAIL"


@log_test
def catalog():
    """Проверяет доступность каталога товаров."""
    return "PASS"


@log_test
def add_card(card_number, currency="RUB", **extra):
    """Проверяет добавление новой банковской карты."""
    if len(card_number) == 16 and card_number.isdigit():
        return f"PASS. Карта {card_number[-4:]} добавлена, валюта: {currency}"
    return "FAIL. Некорректный номер карты"


authorisation("user", "qwerty1234")
print()

catalog()
print()

add_card("1234567890")
print()

add_card("1234567890123456", currency="RUB")
print()

add_card("1234", currency="USD")
print()
