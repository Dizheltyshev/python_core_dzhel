from functools import reduce

tests = [
    {"name": "test_signup", "status": "PASS", "time": 1.4},
    {"name": "test_login", "status": "PASS", "time": 0.8},
    {"name": "test_logout", "status": "SKIP", "time": 1.8},
    {"name": "test_cart", "status": "FAIL", "time": 1.2},
    {"name": "test_news", "status": "PASS", "time": 2.1},
    {"name": "test_delete_order", "status": "FAIL", "time": 2.5}
]

failed_tests = list(filter(lambda t: t["status"] == "FAIL", tests))
failed_names = list(map(lambda t: t["name"], failed_tests))

total_time = reduce(lambda acc, t: acc + t["time"], tests, 0)

passed_names = [t["name"] for t in tests if t["status"] == "PASS"]

passed_count = len([t for t in tests if t["status"] == "PASS"])
failed_count = len(failed_tests)
skipped_count = len([t for t in tests if t["status"] == "SKIP"])

print(f"PASS: {passed_count}")
print(f"FAIL: {failed_count}")
print(f"SKIP: {skipped_count}")
print(f"Упавшие тесты: {failed_names}")
print(f"Успешно пройденные тесты: {passed_names}")
print(f"Общее время выполнения тестов: {total_time}")
