import json
from functools import reduce


def load_tests(testbl):
    try:
        with open(testbl, "r") as file:
            data = json.load(file)
    except FileNotFoundError as e:
        print(f"Ошибка: файл отсутствует — {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка: некорректный JSON — {e}")
        return None

    if not isinstance(data, list):
        print("Ошибка: JSON должен быть списком тестов")
        return None

    for test in data:
        if not isinstance(test, dict):
            print("Ошибка: каждый тест должен быть словарём")
            return None
        if "name" not in test or "status" not in test or "time_wasted" not in test:
            print(f"Ошибка: у теста отсутствуют данные — {test}")
            return None

    return data


def build_report(tests):
    total = len(tests)

    passed = len([t for t in tests if t["status"] == "PASS"])
    failed = len([t for t in tests if t["status"] == "FAIL"])
    skipped = len([t for t in tests if t["status"] == "SKIP"])

    failed_tests = list(filter(lambda t: t["status"] == "FAIL", tests))
    failed_names = list(map(lambda t: t["name"], failed_tests))

    slowest = reduce(
        lambda a, b: a if a["time_wasted"] >= b["time_wasted"] else b,
        tests
    )

    total_time = reduce(lambda acc, t: acc + t["time_wasted"], tests, 0)

    report = {
        "total": total,
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "failed_tests": failed_names,
        "slowest_test": slowest["name"],
        "slowest_duration": slowest["time_wasted"],
        "total_time": round(total_time, 2)
    }

    return report


def save_report(test_results, testbl):
    try:
        with open(testbl, "w") as file:
            json.dump(report, file, indent=4)
        print(f"Отчёт сохранён в {testbl}")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")


tests = load_tests("testbl.json")

if tests is not None:
    report = build_report(tests)
    save_report(report, "test_results.json")