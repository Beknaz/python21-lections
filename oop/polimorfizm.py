"================Полиморфизм===================="
# Полиморфизм - принцип ООП, в котором методы в разных классах называется одинаково. (один интерфейс - разный функционал)
class Dog:
    def speak(self):
        print("gav-gav")
class Cat:
    def speak(self):
        print("myu-myu")
class Frog:
    def speak(self):
        print("kwa-kwa")

animals = [Cat(), Dog(), Cat(), Frog(), Frog()]

for animal in animals:
    animal.speak()