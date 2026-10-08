# Создайте три объекта класса CreditCard. Пополните баланс первой и второй карты, а с третьей карты снимите
# некоторую сумму. После выполнения операций выведите информацию о состоянии всех трёх карт.

class CreditCard:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Счёт {self.account_number}: пополнение на {amount} рублей. Баланс счета: {self.balance} рублей")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"Счёт {self.account_number}: снятие {amount} рублей. Баланс счета: {self.balance} рублей")

    def show_info(self):
        print(f"Счёт: {self.account_number}, баланс: {self.balance} рублей")

card1 = CreditCard("1234567890", 0)
card2 = CreditCard("0987654321", 52500)
card3 = CreditCard("1029384756", 30000)

print("Транзакции:")
card1.deposit(100000)
card2.deposit(25000)
card3.withdraw(30000)
print()

print("Состояние счетов:")
card1.show_info()
card2.show_info()
card3.show_info()