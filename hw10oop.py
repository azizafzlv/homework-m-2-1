"""
Задача 1: Инкапсуляция - Класс Счет

Создайте класс Account с приватным атрибутом balance (баланс)
и методами для депозита и снятия средств, а также для получения
текущего баланса.
"""

# class Account:
#     def __init__(self, in_balance=0):
#         self.__balance = in_balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Сумма депозита должна быть положительной")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Недостаточно средств или отриц-ая сумма")
    
#     def get_balance(self):
#         return self.__balance
    

# account = Account(10000)
# print(f"Текущий баланс {account.get_balance()}")

# account.deposit(200)
# print(f"Баланс после депозита: {account.get_balance()}")

# account.withdraw(5500)
# print(f"Баланс после снятия: {account.get_balance()}")

"""
Задача 2: Полиморфизм - Классы Животных

Создайте классы Dog и Cat, оба наследуют от класса Animal.
Каждый из классов должен иметь метод speak, который возвращает
разные звуки для собаки и кошки.
"""

# class Animal:
#     def __init__(self, name, speak):
#         self.name = name
#         self.speak = speak

#     def info(self):
#         print(f"{self.name} говорит {self.speak}")

# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# animal_dog = Dog(name='Собачка Шарик', speak='Гав-Гав')
# animal_cat = Cat(name='Кошечка Мурка', speak='Мяу-Мяу')

# animal_dog.info()
# animal_cat.info()

"""
Задача 3: Класс Фигура

Создайте класс Shape с методом area, который возвращает площадь.
Создайте производные классы, такие как Rectangle и Circle,
переопределяющие метод area.
"""

# from math import pi

# class Shape:
#     def __init__(self, name) -> None:
#         self.name = name

#     def get_area(self):
#         pass

# #делали на уроке
# class Triangle(Shape):
#     def __init__(self, name, height, a, b, c) -> None:
#         super().__init__(name)
#         self.__a = a
#         self.__b = b
#         self.__c = c
#         self.__height = height

#     def get_area(self):
#         return (1/2) * self.__a * self.__height


# class Circle(Shape):
#     def __init__(self, name, radius) -> None:
#         super().__init__(name)
#         self.__radius = radius

#     def get_area(self):
#         return pi * (pow(self.__radius, 2))

# #в домашке был еще прямоугольник
# class Rectangle(Shape):
#     def init(self, name, a, b) -> None:
#         super().__init__(name)
#         self.__a = a
#         self.__b = b
#     def get_area(self):
#         return self.__a * self.__b
    

"""
Задача 4: Композиция - Класс Комната

Создайте класс Room с атрибутами, представляющими список мебели.
Используйте композицию, создав отдельные классы для разных типов
мебели, и добавьте их в класс Room.
"""

# class Table:
#     def __init__(self, matetial, size):
#         self.material = matetial
#         self.size = size

#     def describe(self):
#         return f"Стол из {self.material}, размер: {self.size}"
    
# class Chair:
#     def __init__(self, material, color):
#         self.material = material
#         self.color = color

#     def describe(self):
#         return f"Стул из {self.material}, цвет: {self.color}"

# class Wardrobe:
#     def __init__(self, material, compartments):
#         self.material = material
#         self.compartments = compartments

#     def describe(self):
#         return f"Шкаф из {self.material}, кол-во отделений: {self.compartments}"

# class Room:
#     def __init__(self, furniture):
#         self.furniture = furniture

#     def describe_furniture(self):
#         for item in self.furniture:
#             print(item.describe())

# table1 = Table("дуб", 120)
# chair1 = Chair("пластик", "белый")
# wardrobe1 = Wardrobe("дерево", 5)

# #использование композиции
# room1 = Room([table1, chair1, wardrobe1])

# room1.describe_furniture()


"""
Задача 5: Абстрактный Класс - Устройство

Создайте абстрактный класс Device с абстрактным методом turn_on.
Создайте производные классы, такие как Laptop и Smartphone,
реализующие метод turn_on.
"""

# from abc import ABC, abstractmethod

# class Device(ABC):
#     @abstractmethod
#     def turn_on(self):
#         pass

# class Laptop(Device):
#     def turn_on(self):
#         print("Laptop включен")

# class Smartphone(Device):
#     def turn_on(self):
#         print("Smartphone включен")

# laptop = Laptop()
# smartphone = Smartphone()

# laptop.turn_on()
# smartphone.turn_on()



