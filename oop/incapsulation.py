"==============Инкапсуляция==============="
# Инкапсуляция - принцип ООП
# 1. сокрытие данных (ограничение доступа к определенным методам и классам)
# 2. сбор всех необходимых для класса методов и аттрибутов в "капсулу"(класс)

"=============Модификаторы доступа к аттрибутам================"

# 1. public (публичный)
# 2. protect (защищенный)
# 3. private (приватный)

class A:
    attr1 = "публичный"
    _attr2 = "защищенный"
    __attr3 = "приватный"
# print(A._A__attr3)

"=============getters / setters================"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 120 and new_age > 0:
            self.__age = new_age
        else:
            raise Exception ("age can not be less than 0 or more than 120")

obj = Person("Beka", 24)
print(obj.age)
obj.age = 5
print(obj.age)