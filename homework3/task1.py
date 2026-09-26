# Программа должна преобразовать введенную строку в список, подсчитать количество тестов
# каждого типа и вывести общую статистику

def get_test_statistics(results):
    statuses = {"PASS": 0, "FAIL": 0, "SKIP": 0}

    for status in results:
        if status in statuses:
            statuses[status] += 1

    return statuses


user_input = input("Введите результаты тестов через пробел: ")
results = user_input.upper().split()

statuses = get_test_statistics(results)

total = len(results)
passed = statuses["PASS"]
percent = int(passed / total * 100)

print(f"Всего тестов: {total}")
print(f"PASS: {statuses['PASS']}")
print(f"FAIL: {statuses['FAIL']}")
print(f"SKIP: {statuses['SKIP']}")
print(f"Успешно: {percent}%")