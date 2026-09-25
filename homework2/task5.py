# 5. Результаты автотестов

test_passed = 0
test_failed = 0
test_skipped = 0
number = int(input("Введите количество автотестов: "))

for number in range(number):
    status = input(f"Результат теста №{number + 1}: ").upper()
    if status == "PASS":
        test_passed += 1
    elif status == "FAIL":
        test_failed += 1
    elif status == "SKIP":
        test_skipped += 1
    else:
        print("Неизвестный статус, пропускаю")

print("Statuses")
print(f"PASS: {test_passed}")
print(f"FAIL: {test_failed}")
print(f"SKIP: {test_skipped}")

if test_failed > 0:
    print("Есть упавшие тесты!")
else:
    print("Все тесты пройдены успешно!")