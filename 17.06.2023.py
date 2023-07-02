import math
import time

'''
def area(fig_type, *args):
    area = 0
    if fig_type == "circle":
        radius = args[0]
        return print(math.pi * radius ** 2)

    elif fig_type == "square":
        side_1, side_2 = args
        return print(side_1 * side_2)

    elif fig_type == "triangle":
        base = args[0]
        height = args[1]
        return print(0.5 * base * height)
    else:
        return print("Wrong figure. Retry please.")

area(input("Figure type: "), int(input("Radius/side_1/base: ")), int(input("side_2/height")))


def palindrom(x):
    if len(x) % 2 != 0:
        print("False")
    else:
        temp_list = []
        for n in x:
            if x.isalfa:
                temp_list.append(n)
                return temp_list == temp_list[::-1]

palindrom(x)


def fact_recurs(n):
    if n == 0:
        return 1
    else:
        return n * fact_recurs(n-1)

fact_recurs(5)
""" Из двух списков выбирает общие элементы и собирвет в третий список без повторов"""
def common (lst1, lst2):
    return list(set(lst1) and set(lst2))


def anagram(a, b):
    if sorted(a.lower) == sorted(b.lower):
        return print('Yes')
    else:
        print('No')

anagram("rtklg", "klrgt")


square = lambda x: x**2

print(square(5))

even = lambda x: x % 2 == 0

print(even(5))
'''
'''
аннотации

def greet (name: str) -> str: ''' '''указан ожидаемый тип вводимого значения'''
'''
    return "Hello," + name

def add(x:, y):
    return x + y
'''
'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
ООП
'''
'''
class MyClass:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print('Hello ' + self.name + '!')

m = MyClass('Alex')
m.hello()
'''
'''
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('I can speak')


class Dog(Animal):
    def speak(self):
        print('Back-Back')

class Cat(Animal):
    def speak(self):
        print('Mew-Mew')


dog = Dog('Richard')
dog.speak()

cat = Cat('Charly')
cat.speak()

print(dog.__dict__)
print(cat.__dict__)
'''
'''
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2


rectangle = Rectangle(4, 5)
print(rectangle.area())

circle = Circle(3)
print(circle.area())
'''
'''
class Book:
    def __init__(self,
                 title,
                 year,
                 publisher,
                 genre,
                 author,
                 price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def display(self):
        print(
            'Author: ', self.author, '\n'
            'Name: ', self.title, '\n'
            'Price: ', self.price
        )

    def get_title(self):
        return self.title

book = Book('Test',
            2023,
            'TOP',
            'Drame',
            'Komarov A.N.',
            9500
            )

book.display()
print(book.get_title())

while True:
    choice = input(
        '1 - show book\n'
        '2 - title\n'
    )
    
    if choice == '1':
        book.display()
    if choice == '2':
        print(book.get_title())
'''


class Device:
    def __init__(self,
                 brand,
                 title,
                 price,
                 availability):
        self.brand = brand
        self.title = title
        self.price = price
        self.availability = availability


class CoffeeMachine(Device):
    def set_parameters(self, water_volume, coffee_volume, cup_volume):
        self.water_volume = water_volume
        self.coffee_volume = coffee_volume
        self.cup_volume = cup_volume

    def get_coffee(self):
        print('Getting coffee')
        time.sleep(7)
        return self.water_volume * 0.3 + self.coffee_volume * 0.131


Delongy_2023 = CoffeeMachine('Coffee2023',
                             'Delongy',
                             70000,
                             True)  # Создал объект кофемашина
Delongy_2023.set_parameters(500, 200, ['Small', 'Medium', 'Large'])  # Задал параметры объекта CoffeeMachine

print(Delongy_2023.get_coffee())
