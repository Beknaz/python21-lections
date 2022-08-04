# import random
# chislo = random.randint(1,11)
# popytki = 0
# name1 = input('Введите ваше имя:' )
# otvet = input('Хочешь ли ты сыграть со мной в игру? да или нет:' )
# while otvet =='да':
#     inp = int(input('угадай число от 1 до 10 которое я загадал:' ))
#     popytki += 1
#     if inp < chislo:
#         print('Введенное тобою число меньше загаданного мною числа')
#     if inp > chislo:
#         print('Введенное тобою число больше загаданного мною числа')    
#     if inp == chislo:
#         print('Поздравляю',name1, 'ты угадал загаданное мною число за', popytki, 'попытки')
#         popytki = 0
#         chislo = random.randint(1,11)
#         otvet = input('Хочешь ли ты сыграть со мной в игру? да или нет:' )  
# else:
#     print('Досвидания', name1)
    

class Circle:
    color = 'Синий'
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return Circle.pi * pow(self.radius, 2)

circle = Circle(2)
circle.color = 'Красный'

print(circle.color)
print(circle.get_area())