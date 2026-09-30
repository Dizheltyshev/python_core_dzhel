# Программа должна случайным образом выбрать указанное количество уникальных тестов из списка
# и каждому выбранному тесту случайно назначить статус PASS, FAIL или SKIP.
import random

tests = [
    "test_login",
    "test_logout",
    "test_registration",
    "test_profile",
    "test_payment",
    "test_search"
]
passed = 0
failed = 0
skipped = 0

count = int(input("Сколько тестов запустить? "))

if count > len(tests):
    print("Ошибка: в списке всего 6 тестов")
else:
    test_cases = random.sample(tests, count)
    statuses = ["PASS", "FAIL", "SKIP"]

    for test in test_cases:
        status = random.choice(statuses)
        print(f"{test} — {status}")

        if status == "PASS":
                passed += 1
        elif status == "FAIL":
                failed += 1
        elif status == "SKIP":
                skipped += 1

print(f"\nВсего запущено тестов: {count}")
print(f"PASS: {passed}")
print(f"FAIL: {failed}")
print(f"SKIP: {skipped}")