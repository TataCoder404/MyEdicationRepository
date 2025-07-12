# ----------------------- 1 ---------------------------------------

# class MyCats:
#     def __init__(self, name, type, age=1, sound="..."):
#         self.name = name
#         self.type = type
#         self.age = age
#         self.sound = sound

#     def voice(self):
#         print(f"Меня зовут {self.name}, я говорю {self.sound}")

# cat1 = MyCats(name="Vasya", type="rus", age=2, sound="Мяу")
# cat2 = MyCats(name="Gosha", type="usa", age=4, sound="Meow")
# cat3 = MyCats(name="Dora", type="germ", age=2)

# cat1.voice()
# cat2.voice()
# cat3.voice()


# ----------------------- 2 ---------------------------------------

# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def perimeter(self):
#         P = self.a * 2 + self.b * 2
#         return P

#     def square(self):
#         S = self.a * self.b
#         return S

#     def info(self):
#         print(f"сторона 1: {self.a}\n"
#             f"сторона 2: {self.b}\n"
#             f"периметр: {self.perimeter()}\n"
#             f"площадь: {self.square()}")

# myFigure = Rectangle(a = 3, b = 2)

# myFigure.info()

# ----------------------- 3 ---------------------------------------


# class Car:
#     def __init__(self, name, power, fuel_consume_per_100km, volume, current_volume):
#         self.name = name
#         self.power = power
#         self.fuel_consume_per_100km = fuel_consume_per_100km
#         self.volume = volume  # объём бензобака
#         self.current_volume = current_volume # текущий уровень топлива
#     def fuel_consume(self, S):
#         fuel = S / 100 * S
#         return fuel

#     def drive(self, S):
#         V = self.fuel_consume_per_100km/100 * S
#         V2 = self.current_volume - V
#         if V2 < 0:
#             print("Поездка невозможна")
#         else:
#             print(V2)

# March = Car(name="March", power=90, fuel_consume_per_100km=9, volume=40, current_volume=30)
# Crown = Car(name="Crown", power=180, fuel_consume_per_100km=14, volume=70, current_volume=40)
# Mini = Car(name="Mini", power=60, fuel_consume_per_100km=8, volume=35, current_volume=1)


# March.drive(50)
# Crown.drive(50)
# Mini.drive(50)

# ----------------------- 4 ---------------------------------------


# class Person:
#     def __init__(self):
#         self.wardrobe = []
    
#     def append_clother(self, i):
#         self.wardrobe.append(i)

#     def get_heat_protection(self):
#         return sum(i.heat_protection for i in self.wardrobe)
        
#     def get_cold_protection(self):
#         return sum(i.cold_protection for i in self.wardrobe)

# class Clothes:
#     def __init__(self, name, heat_protection, cold_protection):
#         self.name = name
#         self.heat_protection = heat_protection
#         self.cold_protection = cold_protection


# tshort = Clothes(name = "tshort", heat_protection = 2, cold_protection = 0)
# coat = Clothes(name = "coat", heat_protection = 0, cold_protection = 10)
# dress = Clothes(name = "dress", heat_protection = 2, cold_protection = 1)
# pants = Clothes(name = "pants", heat_protection = 1, cold_protection = 2)
# hat = Clothes(name = "hat", heat_protection = 5, cold_protection = 1)

# human1 = Person()

# human1.append_clother(coat)
# human1.append_clother(dress)

# for item in human1.wardrobe:
#     print(item.name)

# print(f"Общая теплозащита: {human1.get_heat_protection()}")
# print(f"Общая холодозащита: {human1.get_cold_protection()}")


# ----------------------- 5 ---------------------------------------

# class VendingMachine:
#     def __init__(self, name):
#         self.name = name
#         assortment(self) = {}

#     def add_item(self, item_name, price):
#         self.assortment[item_name] = price
    
#     def sell_item(self, item_name, buyer):
#         if item_name not in self.assortment:
#             print(f"Товара '{item_name}' нет в автомате {self.name}")
#             return False
        
#         price = self.assortment[item_name]
#         if buyer.money >= price:
#             buyer.money -= price
#             buyer.things.append(item_name)
#             print(f"{buyer.name} купил '{item_name}' в автомате {self.name} за {price} руб.")
#             return True
#         else:
#             print(f"У {buyer.name} недостаточно денег для покупки '{item_name}'")
#             return False


# class Person:
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#         self.things = []
    
#     def buy_item(self, machine, item_name):
#         """Покупает товар в указанном автомате"""
#         machine.sell_item(item_name, self)
    
#     def show_items(self):
#         """Показывает все вещи человека"""
#         if not self.things:
#             print(f"{self.name} пока ничего не купил")
#         else:
#             print(f"У {self.name} есть: {', '.join(self.things)}")

# # Создаем торговые автоматы
# snack_machine = VendingMachine("Автомат с едой")
# drink_machine = VendingMachine("Автомат с напитками")

# # Наполняем автоматы товарами
# snack_machine.add_item("Шоколадка", 50)
# snack_machine.add_item("Чипсы", 70)
# snack_machine.add_item("Печенье", 30)

# drink_machine.add_item("Кола", 60)
# drink_machine.add_item("Вода", 30)
# drink_machine.add_item("Сок", 45)

# # Создаем людей
# alice = Person("Алиса", 200)
# bob = Person("Боб", 150)

# # Люди покупают товары
# alice.buy_item(snack_machine, "Шоколадка")
# alice.buy_item(drink_machine, "Кола")

# bob.buy_item(snack_machine, "Чипсы")
# bob.buy_item(drink_machine, "Вода")

# # Пробуем купить товар, которого нет
# alice.buy_item(snack_machine, "Мороженое")

# # Пробуем купить товар без денег
# bob.buy_item(drink_machine, "Сок")
# bob.buy_item(drink_machine, "Сок")  # Пробуем второй раз

# # Показываем вещи людей
# print()
# alice.show_items()
# bob.show_items()



# ----------------------- на занятии 1 ---------------------------------------


# class Tablo:
#     def __init__(self, home=0, guest=0):
#         self.home = home
#         self.guest = guest

#     def add_home(self, n):
#         self.home += n

#     def add_guest(self, n):
#         self.guest += n

#     def show_score(self):
#         winner = ""
#         if self.home > self.guest:
#             winner = "home"
#             print(f"Счёт в матче {self.home}:{self.guest} в пользу {winner}")
#         elif self.home < self.guest:
#             winner = "guest"
#             print(f"Счёт в матче {self.home}:{self.guest} в пользу {winner}")
#         else:
#             print(f"Счёт в матче {self.home}:{self.guest}")
        

#     def drop_score(self):
#         self.home = 0
#         self.guest = 0


# khv_vdk = Tablo()

# khv_vdk.add_home(3)
# khv_vdk.add_guest(1)

# khv_vdk.show_score()
# khv_vdk.drop_score()

# khv_vdk.show_score()
