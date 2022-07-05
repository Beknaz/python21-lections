"=============OOP=================="
# OOP - Objekt - oriented programming
# ООП - обьектно-ориентированное программирование(парадигма)
from lib2to3.pgen2.token import AMPER


class Person:
    # name = "Beknaz3404"
    # age = 24
    arms = 2
    legs = 2
    def __init__(self, name, age):

        """
    Функция, которая вызывается когда мы создает обьект от класса self - ссылка на созданный обьект 
        """        
        self.name = name
        self.age = age
    def add_age(self):
        self.age +=1
    def walk():
        print("я иду")
    def add_age(self):
        self.age +=1
    
    def __str__(self):
        """
функция, которая вызывается, когда мы оборачиваем обьект в класс str или когда принтуем обьект
функция __str__ ничего кроме self не принимает и обязательно должна возвращать строку
"""
        return f"{self.name} - {self.age} y.o"
        person1 = Person("Настя", 50)
        print(person1)

        person2 = Person("Жаркынай", 15)
        print(person2)
        person1 = Person()
        person1.add_age()
        print(person1.age)

        Person.age = 17
        print(Person.age)

        person2 = Person()
        print(person2.age)

"=============Аттрибуты класса=================="
# аттрибуты класса - переменные внутри класса
"=============Методы класса=================="
# методы класса - функции внутри класса
"=============Обьекты класса=================="
# обьект/экземпляр/instance класса - обьект созданный по шаблону класса(он перенимает все аттрибуты и методы у класса)
"=============Аттрибуты и Обьекты класса=================="
# аттриибуты и методы, которые есть у обьекта, но возможно их нет у класса. 

class A:
    var1 = "переменная класса"

    def __init__(self):
        self.var2 = "переменная обьекта"

print(dir(A)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']

obj = A()
print(dir(obj)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1', 'var2']

"Класс имеет доступ только к аттрибутам класса"
"Обьект имеет доступ и к аттрибутам класса, и к его аттрибутам"
