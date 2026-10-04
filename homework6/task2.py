# Создайте два независимых замыкания с разными значениями max_time и продемонстрируйте их работу.

def create_time_checker(max_time):
    def check_time(actual_time):
        if actual_time <= max_time:
            print(f"Успех: тест не превышает лимит {max_time} секунд")
            return True
        else:
            print(f"Ошибка: тест превышает лимит {max_time} секунд")
            return False

    return check_time

closure1 = create_time_checker(10)
closure2 = create_time_checker(25)

print("Проверка смок-тестов (лимит 10 сек):")
closure1(5)
closure1(9)
closure1(11)

print()
print("Проверка регрессионных тестов (лимит 25 сек):")
closure2(24)
closure2(25)
closure2(26)