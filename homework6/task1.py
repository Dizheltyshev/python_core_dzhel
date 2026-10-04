# Напишите рекурсивную функцию, которая подсчитывает количество тестов со статусом PASS.
# Функция должна обрабатывать список с помощью рекурсии.

tests = [
    {"name": "test1", "status": "SKIP"},
    {"name": "test2", "status": "PASS"},
    {"name": "test3", "status": "PASS"},
    {"name": "test4", "status": "FAIL"},
    {"name": "test5", "status": "PASS"}
]

def count_passed(tests):
    if len(tests) == 0:
        return 0

    first_test = tests[0]
    if first_test["status"] == "PASS":
        first_is_pass = 1
    else:
        first_is_pass = 0

    rest = tests[1:]
    rest_passed = count_passed(rest)

    return first_is_pass + rest_passed

result = count_passed(tests)
print(f"Количество тестов PASS = {result}")