# Разработать программу для работы с цветами и букетами, используя
# принципы объектно-ориентированного программирования.
class Flower:
    def __init__(self, name, price, lifetime):
        self.name = name
        self.price = price
        self.lifetime = lifetime

    def show_info(self):
        print(f"{self.name}: цена - {self.price} рублей, время жизни - {self.lifetime} дней")


class Tulip(Flower):
    def __init__(self):
        super().__init__("Тюльпан", 70, 6)


class Peony(Flower):
    def __init__(self):
        super().__init__("Пион", 230, 8)


class Rose(Flower):
    def __init__(self):
        super().__init__("Роза", 150, 7)


class Orchid(Flower):
    def __init__(self):
        super().__init__("Орхидея", 170, 9)


class Daisy(Flower):
    def __init__(self):
        super().__init__("Ромашка", 60, 10)


class Gerbera(Flower):
    def __init__(self):
        super().__init__("Гербера", 110, 6)


class Accessory:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"Аксессуар: {self.name}, цена - {self.price} рублей")


class Bouquet:
    def __init__(self):
        self.flowers = []
        self.accessories = []

    def add_flower(self, flower):
        self.flowers.append(flower)
        print(f"Добавлен цветок: {flower.name}")

    def add_accessory(self, accessory):
        self.accessories.append(accessory)
        print(f"Добавлен аксессуар: {accessory.name}")

    def total_price(self):
        flowers_sum = 0
        for flower in self.flowers:
            flowers_sum = flowers_sum + flower.price

        accessories_sum = 0
        for accessory in self.accessories:
            accessories_sum = accessories_sum + accessory.price

        return flowers_sum + accessories_sum

    def average_lifetime(self):
        if len(self.flowers) == 0:
            return 0

        total_lifetime = 0
        for flower in self.flowers:
            total_lifetime = total_lifetime + flower.lifetime

        return total_lifetime / len(self.flowers)

    def sort_by_price(self):
        self.flowers.sort(key=lambda f: f.price, reverse=True)

    def has_flower(self, flower_name):
        for flower in self.flowers:
            if flower.name == flower_name:
                return True
        return False

    def show_bouquet(self):
        print("Состав букета.")
        print("Цветы:")
        for flower in self.flowers:
            flower.show_info()

        print()
        print("Аксессуары.")
        for accessory in self.accessories:
            accessory.show_info()

        print()
        print(f"Общая стоимость: {self.total_price()} рублей")
        print(f"Среднее время жизни: {int(self.average_lifetime())} дней")
        print()


bouquet = Bouquet()

bouquet.add_flower(Tulip())
bouquet.add_flower(Peony())
bouquet.add_flower(Rose())
bouquet.add_flower(Orchid())
bouquet.add_flower(Daisy())
bouquet.add_flower(Gerbera())

bouquet.add_accessory(Accessory("Упаковка", 200))
bouquet.add_accessory(Accessory("Лента", 100))
bouquet.add_accessory(Accessory("Подкормка для срезанных цветов", 20))
bouquet.add_accessory(Accessory("Открытка", 50))

print()
bouquet.show_bouquet()

print("Сортировка по цене")
bouquet.sort_by_price()
print("Цветы после сортировки:")
for flower in bouquet.flowers:
    flower.show_info()
print()

print("Проверка наличия цветка")
print(f"В букете есть Тюльпан? {bouquet.has_flower('Тюльпан')}")
print(f"В букете есть Пион? {bouquet.has_flower('Пион')}")
print(f"В букете есть Хризантема? {bouquet.has_flower('Хризантема')}")
print()