import functools
import random


def retry(count):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, count + 1):
                print(f"Попытка №{attempt}")

                result = func(*args, **kwargs)

                if result is True:
                    print(f"Успех на попытке №{attempt}")
                    return True

            print(f"Все {count} попыток исчерпаны")
            return False

        return wrapper

    return decorator


@retry(7)
def amount_products(test_name, min_number=7):
    rand = random.randint(1, 10)
    print(f"{test_name}: выпало число {rand}")

    if rand > min_number:
        return True
    return False


print("Запуск теста")
print("Условие: нужно больше 7 товаров для скидки")
amount_products("Количество товаров для скидки", min_number=7)
print()

print("Ещё один запуск")
print("Условие: нужно 7 товаров для скидки")
amount_products("Количество товаров для скидки")
print()