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

"=============Принципы ООП=================="
# наследование
# инкапсуляция
# полиморфизм
# Абстракция
# Ассоциация