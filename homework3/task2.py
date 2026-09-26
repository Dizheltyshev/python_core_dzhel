# Необходимо с помощью zip() объединить название каждого тест-кейса с его статусом.
test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]

def print_report(test_cases, statuses):
    passed = 0
    failed = 0

    for case, status in zip(test_cases, statuses):
        print(f"{case} — {status}")

        if status == "PASS":
            passed += 1
        elif status == "FAIL":
            failed += 1

    print(f"Успешных: {passed}")
    print(f"Неуспешных: {failed}")

    if failed > 0:
        print("Тестовый запуск неуспешен")
    else:
        print("Тестовый запуск успешен")

print_report(test_cases, statuses)