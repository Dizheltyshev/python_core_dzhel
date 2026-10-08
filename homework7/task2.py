# Создайте объект ATM, добавьте в него несколько купюр и выполните несколько операций снятия денег.

class ATM:
    def __init__(self, count_100, count_50, count_20):
        self.count_100 = count_100
        self.count_50 = count_50
        self.count_20 = count_20

    def add_money(self, add_20, add_50, add_100):
        self.count_100 = self.count_100 + add_100
        self.count_50 = self.count_50 + add_50
        self.count_20 = self.count_20 + add_20
        print(f"Внесено: 100x{add_100}, 50x{add_50}, 20x{add_20}")
        self.show_info()

    def show_info(self):
        total = self.count_100 * 100 + self.count_50 * 50 + self.count_20 * 20
        print(f"Баланс ATM: {total}")

    def withdraw(self, amount):
        n100 = min(amount // 100, self.count_100)
        amount = amount - n100 * 100

        n50 = min(amount // 50, self.count_50)
        amount = amount - n50 * 50

        n20 = min(amount // 20, self.count_20)
        amount = amount - n20 * 20

        if amount != 0:
            print(f"Невозможно выполнить операцию. Попробуйте другую сумму.")
            return False

        self.count_100 = self.count_100 - n100
        self.count_50 = self.count_50 - n50
        self.count_20 = self.count_20 - n20

        print(f"Выдано: 100x{n100}, 50x{n50}, 20x{n20}")
        return True

atm = ATM(100, 125, 150)

print("Операция 1. Пополнение купюр")
atm.add_money(2, 12, 10)
print()

print("Операция 2. Выдача купюр")
result = atm.withdraw(1435)
print(f"Результат: {result}")
atm.show_info()
print()

print("Операция 3. Пополнение купюр")
atm.add_money(0, 0, 40)
print()

print("Операция 4. Выдача купюр")
result = atm.withdraw(3470)
print(f"Результат: {result}")
atm.show_info()
print()

print("Операция 5. Пополнение купюр")
atm.add_money(34, 7, 0)
print()