def run_test(attempts, timeout):
    if attempts < 0 or attempts > 5:
        raise ValueError(f"Количество запусков должно быть от 0 до 5, а получено {attempts}")

    if timeout <= 0:
        raise ValueError(f"Таймаут должен быть положительным.")

    print(f"Тест начался: запусков = {attempts}, таймаут = {timeout}")


# Тест 1: ввалидные данные
try:
    run_test(4, 14)
except ValueError as e:
    print(f"Ошибка: {e}")

# Тест 2: отрицательный таймаут
try:
    run_test(5, -11)
except ValueError as e:
    print(f"Ошибка: {e}")

# Тест 3: большое количество повторных запусков
try:
    run_test(17, 25)
except ValueError as e:
    print(f"Ошибка: {e}")