class InvalidTestStatusError(Exception):
    pass

def check_status(status):
    valid_statuses = ["PASS", "FAIL", "SKIP"]

    if status not in valid_statuses:
        raise InvalidTestStatusError(f"Некорректный статус теста: {status}")

    print(f"Допустимый статус: {status}")

test_statuses = ["PASS", "FAIL", "SKIP", "BLAH"]

for status in test_statuses:
    try:
        check_status(status)
    except InvalidTestStatusError as e:
        print(f"Ошибка. {e}")