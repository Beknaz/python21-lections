# # #task1

# # data = input('Введите имя, фамилию и возраст через пробел:\n').split()
# # name = data[0]
# # last = data[1]
# # yers = data[-1]
# # name = name.lower().replace('a', '').title()
# # last = '*'.join(list(last))
# # print((name + last) * int(yers))

# # # task2

# # string = input('введите строку: ').lower()
# # a = string.count('a')
# # o = string.count('o')
# # i = string.count('i')
# # e = string.count('e')
# # y = string.count('y')
# # u = string.count('u')
# # print(f'В вашей строке насчитано {a+o+i+e+y+u} гласных букв')

# # #task3

# # login = input('Введите ваш юзернейм одним словом: ')
# # center = int(len(login)/2)
# # login2 =login[:center] + '&' +login[center:] + '$'
# # pasword = login2.swapcase()
# # print(f'Вам сгенерирован пороль: {pasword}')


# # name = input()
# # last_name = input()
# # age = input()
# # city = input()
# # print(f'Вас зовут {name} {last_name}, Ваш возраст: {age}, Вы проживаете в городе {city}')

# # string = input()
# # print(len(string) > 5)

# #========3=======
# # mark = int(input())
# # if mark >= 90:
# #     print('Отлично, ваша оценка 5!')
# # elif mark >= 80:
# #     print('Здоровоб ваша оценка 4!')
# # elif mark >= 70:
# #     print('Хорошо, ваша оценка 3!')
# # elif mark >= 60:
# #     print('Вам стоит подучить материал')
# # else:
# #     print('Вы не сдали экзамен')

# #==========4======
# # number = int(input('число: '))
# # if number <= -1:
# #     print('negative')
# # elif number >= 1:
# #     print('positive')
# # elif number == 0:
# #     print('zero')


# # =========7=====
# # x = 12
# # y = 12
# # z = 12
# # if x == y and x == z:
# #     print('3')
# # elif x == y or x == z:
# #     print('2')
# # else:
# #     print('0')



# # x = int(input())
# # y = int(input())
# # if x%y == 0:
# #     print(f'{x} делится на {y}')
# #     print(f"Частное:", (x//y))
# # else:
# #     print(f'{x} не делится на {y}')
# #     print(f"Частное:", (x//y))
# #     print(f'Остаток:', (x%y))


# # for i in range(1, 101):
# #     if i%3 == 0 and i%5 == 0:
# #         print('FizzBuzz')
# #     elif i%3 == 0:
# #         print('Fizz')
# #     elif i%5 == 0:
# #         print('buzz')
# #     else:
# #         print(i)

# # year = int(input())
# # if year%4 == 0 and year%100 > 0 or year%400 == 0:
# #     print(f'YES')
# # else:
# #     print(NO)


# # num = int(input())
# # a = ord('a')
# # z = ord('z')
# # A = ord('A')
# # Z = ord('Z')
# # if a<=num<=z or A<=num<=Z:
# #     print('Это буква', chr(num))
# # else:
# #     print('Это не буква а символ', chr(num))

# # greeting = str(input())
# # if greeting is str('Hi'):
# #     print('Привет!')
# # else:
# #     print('NO')

# # parol = str(input('Введите пароль: '))
# # if parol.isalpha():
# #     print('Ваш пароль должен хранить только числа')
# # elif (not parol.isdigit() and not parol.isalpha()) and len(parol) < 8:
# #     print('Ваш пароль должен хранить только числа \nВаш пароль должен содержать не менее 8 символов')
# # elif len(parol) < 8:
# #     print('Ваш пароль должен содержать не менее 8 символов')
# # else:
# #     print('Ваш пароль сохранен')

# # a = input('Введите ваши балы через запятую:' ).split(',')
# # x = ((int(a[0]) + int(a[1]) + int(a[2])) / 3)
# # if x >= 69:
# #     print(f'Вы допущены к экзаменам. Ваш средний балл составляет {x}')
# # else:
# #     print('Вы недопущены ')

# # import random
# # moi = input("Сделайте выбор — камень, ножницы или бумага: ")
# # wariki = ["камень", "бумага", "ножницы"]
# # komp = random.choice(wariki)
# # print(f"\nВы выбрали {moi}, компьютер выбрал {komp}.\n")
# # if moi == komp:
# #     print(f"Оба пользователя выбрали {moi}. Ничья!!")
# # elif moi == "камень":
# #     if komp == "ножницы":
# #         print("Камень бьет ножницы! Вы победили!")
# #     else:
# #         print("Бумага оборачивает камень! Вы проиграли.")
# # elif moi == "бумага":
# #     if komp == "камень":
# #         print("Бумага оборачивает камень! Вы победили!")
# #     else:
# #         print("Ножницы режут бумагу! Вы проиграли.")
# # elif moi == "ножницы":
# #     if komp == "бумага":
# #         print("Ножницы режут бумагу! Вы победили!")
# #     else:
# #         print("Камень бьет ножницы! Вы проиграли.")

# # name_of_list = ['Beknaznazarbek']
# # for n in name_of_list:
# #     x = (len(n) // 2) + (len(n) % 2) 
# #     new_list = n[x:] + n[:x]
# #     print(list(new_list))

# # a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# # b = a.copy()
# # for c in a.keys():
# #     print(c)

# #     for b in a.values():
# #         if b % 2 == 0:
# #             b = 2
# #     print(c + b)

# # task3 list
# name_of_list = ['HelloWorld!']
# a = int((len(name_of_list[0])) / 2)
# if int(len(name_of_list[0])) % 2 != 0:
#     a = int((len(name_of_list[0])) / 2) + 1
# b = name_of_list[0][:a]
# c = name_of_list[0][a:]
# new_list = c + b
# print(list(new_list))


# # university = {'програмирование':25, 'экономика':30, 'медицина':40}
# # university['програмирование'] = 20
# # uni2 = {'лингвистика':50}
# # university.update(uni2)
# # university.pop('медицина')
# # num = list(university.values())
# # print((int(num[0])) + (int(num[1])) + (int(num[2])))



# # y = {1: 'a', 2: 'b', 3: 'c'}
# # b = list(y.values())
# # c = list(y.keys())
# # x = {b[0]:c[0], b[1]:c[1], b[2]:c[2]}
# # print(x)

# # number_of_guests = int(input('Количество гостей: '))
# # guest_dictionary = {}
# # for i in range(number_of_guests):
# #   names = input('Введите имя гостя: ')
# #   guest_dictionary[i+1] = names
# # print(guest_dictionary)

# # kolichestvo = int(input('kolichestvo:' ))
# # spisok = {}
# # for b in range(kolichestvo):
# #     gosti = input('imena gostey poocheredno:' )
# #     spisok[b+1] = gosti
# # print(spisok)
    
# # dictionary = {
# #   "potato": 3,
# #   "milk": 5,
# #   "tomato": 4,
# #   "carrot": 2
# # }
# # number_of_groceries = len(list(dictionary.keys()))
# # print(dictionary)
# # for i in range(number_of_groceries):
# #   user_input = input()
# #   dictionary.pop(f'{user_input}')
# #   print(dictionary)

# # list_ = range(54, 9184)
# # list1 = []
# # for b in list_:
# #     if b % 5 == 0:
# #         list1.append(b)
# # print(list(list1))

# # sum = 200
# # while sum >= 0:
# #     num = int(input())
# #     sum = sum - num
# #     if num > sum:
# #         print('error')
# #     else:
# #         print('остаток:', sum)

# """
# 1) Дан список в котором хранится строка. Разрежьте его на две равные части (если длина строки нечетная, то длина первой части должна быть на один символ больше). Переставьте эти две части местами, при этом каждый символ должен являться отдельной строкой, результат запишите в новый список и выведите на экран.
# """
# name_of_list = ['BeknazNazarbek']
# a = int((len(name_of_list[0])) / 2)
# if int(len(name_of_list[0])) % 2 != 0:
#     a = int((len(name_of_list[0])) / 2) + 1
# b = name_of_list[0][:a]
# c = name_of_list[0][a:]
# new_list = c + b
# print(list(new_list))

# """
# 2) Дан список, состоящий ровно из двух строк. Переставьте эти слова местами. Результат запишите в список и выведите получившийся результат.
# """
# list_ = ['asdf', 'asdfr']
# list1 = list(list_.copy())
# list1.reverse()
# print(list1)
# """
# 3) Даны два множества. С помощью определенного метода (оператора) найдите пересечение множеств:
# """
# a = {1, 2, 3, 4, 5, 6}  
# b = {4, 3, 6 ,1, 8, 9}
# print(a.intersection(b)) 
# print(a & b)
# """
# 4) Четверо коллег собрались на обед. Но они не могут решить, где им пообедать, так как у каждого свои вкусовые предпочтения. Помогите найти им выход в данной ситуации. Данные:

# -Тилек хочет покушать в Dodo или в ImperiaPizza, ну или в крайнем случае FreshBox.
# -Тимур хочет покушать шашлык в OchakKebab или рамен в FreshBox.
# -Александр очень хочет вафли с FreshBox либо KFC.
# -Элину устраивает любой из вариантов. 

# Напишите код, который сможет определить, в какое место им лучше пойти.
# """
# Tilek = ['Dodo', 'ImperiaPizza', 'Freshbox']
# Timur = ['OchakKebab', 'Freshbox']
# Alex = ['Freshbox', 'KFC']
# Elina= ['Freshbox', 'KFC', 'OchakKebab', 'ImperiaPizza', 'Dodo']
# dict = {}
# for i in Tilek:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# for i in Timur:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# for i in Alex:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# for i in Elina:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# print(max(dict, key=dict.get))


# pizda = {'Tilek': ['Dodo', 'ImperiaPizza', 'Freshbox'],
# 'Timur': ['OchakKebab', 'FreshBox'],
# 'Alex': ['Freshbox', 'KFC'],
# 'Beknaz': ['Freshbox', 'KFC', 'OchakKebab', 'ImperiaPizza', 'Dodo']}
# dict = {}
# for element in pizda:
#     for i in pizda[element]:
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1
# print(max(dict, key=dict.get))
# """
# 5) Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным.
# """
# fruit = {'banan': 45, 'alma': 50, 'almurut': 61}
# new_fruit = {k:v for k, v in fruit.items() if v % 2 != 0}
# print(new_fruit)

# """
# 6) Создайте словарь, где значениями будут являться числа. Найдите сумму этих значений.
# """
# a = {'b':5, 'a':10, 'c':4}
# b = {v for v in a.values()}
# print(int(sum(b)))
# """
# 7) Создайте словарь из чисел от 1 до 10, где ключами будут сами числа, а значениями их квадраты.
# """
# a = {i:i ** 2 for i in range(1,11)}
# print(a)
# """
# 8) Дан словарь, значениями в котором являются другие словари. Замените внутренние словари их значениями. Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}} -> {'first': 1, 'second': 2}
# """
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# new_dict = {k:val for k, v in my_dict.items() for val in v.values()}
# print(new_dict)
# """
# 9) Дан словарь. Попытайтесь получить значение по ключу. Обработайте ошибку, возникающую в том случае, если такого ключа нет.
# """
# dict2 = {1:2, 3:453254, 5:64365}
# a = int(input())
# if a in dict2:
#  print(dict2[a])
# else:
#  print('ключа', a, 'не существует')

# # if dict2.get(a) == None:
# #     print('Ключа', a, 'не существует')
# # else:
# #     print(dict2.get(a))


# """
# 10) Запросите у пользователя сумму, которая у него сейчас есть в бумажнике. Если он введёт сумму, меньшую чем 0, то выбросите исключение с текстом "Сумма не может быть отрицательной!"
# """
# summa = int(input())
# if summa < 0:
#     print("Сумма не может быть отрицательной!")
# else:
#     print('У вас есть', summa, 'сомов')



# def capitalizeTitle(self, title: str) -> str:
#     return ' '.join([word.lower() if len(word) < 3 else word.title() for word in title.split()])


# """
# 1) Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
# """
# def sum1(a, b):
#   return a + b
# print(sum1(6, 4))

# # Второй вариант более универсальный
# from functools import reduce
# def multiply_list(nums):
#     total = reduce(lambda a, b: a + b, nums)
#     return total

# numbers = [4, 6, 4, 10]

# print(multiply_list(numbers))



# """
# 2) Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
# """
# def type1(a, b):
#   print(type(a))
#   print(type(b))
# type1(4, 'fdga')

# """
# 3) Напишите функцию, которая принимает список чисел и возвращает их произведение.
# """
# def mul1(a, b):
#   return(a * b)
# print(mul1(3, 10))
# # второй вариант
# # Import Reduce есть выше.
# def multiply_list(nums):
#     total = reduce(lambda a, b: a * b, nums)
#     return total

# numbers = [4, 6, 4, 10]

# print(multiply_list(numbers))

# """
# 4) Мурат с друзья на выходных решил собратся и пойти в ночной клуб.
# Но в ночной клуб пропускают только тех, кому 17+.
# Мурату - 24 лет, Эржану - 21 лет, Чынгызу - 24 лет, Алтынай - 17 лет, Асеме - 16 лет.
# Напишите программу которая определяет кого пустить в ночной клуб а кого нет.
# """
# fans_1 = {'Murat': 24, 'Erzhan': 21, 'Chyngyz': 24, 'Altynay': 17, 'Asema': 16}
# for name, age in fans_1.items():
#   if age < 17:
#     print(f'{name}, Вы не может пройти в клуб')
#   else:
#     print(f'{name}, Вы можете пройти в клуб')

# """
# 5) Напишите функцию, которая принимает строку и выводит количество гласных, согласных букв и остальных символов. Используйте только кириллические символы
# """
# def count_symbols(str_):
#     vowels = 0
#     consonants = 0
#     symbols = 0
    
#     for l in str_.lower():
#         if l in "йуеыаоэяиюё":
#             vowels += 1 
#         elif l in "цкнгшщзмчвфжрлдтсп":
#             consonants += 1
#         else:
#             symbols += 1
#     return f'Количество гласных: {vowels}, согласных: {consonants}, остальных символов: {symbols}'

# print(count_symbols('ма46476иые ркоч пиав оену'))

# """
# 6) Дан списка из чисел. Проверьте, что все числа больше трёх.
# """
# list_ = [5, 5423, 65, 5, 45]
# result = all(num > 3 for num in list_)
# print(result)
  
# """
# 7) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.
# """
# list2 = ['Maksat', 'Aza', 'Beka']
# def vtoroy_varik(a, b):
#   if len(a)>len(b):
#     return a
#   else:
#     return b
# # Import Reduce есть выше.
# result = reduce(vtoroy_varik, list2)
# print(result)
# # второй вариант 
# res = max(list2, key=len)
# print(res)


class Clock:
    def current_time(self):
        import time
        a = time.localtime()
        current_time = time.strftime("%H:%M:%S", a)
        print(current_time)
    
class Alarm:
    def on(self):
       print('Будильник включен')
           
    def off(self):
        print('Будильник выключен')

class AlarmClock(Clock, Alarm):
    def alarm_on(self):
        self.on()


clock = AlarmClock()

clock.current_time() 
clock.alarm_on()

"""
1) Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник.
"""

"""
2) Напишите класс Student, который описывает студента. У студента есть следующие атрибуты: имя, фамилия, класс, и оценки по предметам в следующем виде: {math’: 100, ‘history’: 89, literature’: 88}. 
Сделайте так, чтобы сравнение студентов между собой производилось по средней оценке студента по предметам.
"""

"""
3) Напишите класс учеников Makers, который будет содержать 4 атрибута: 

- атрибут экземпляра name (имя студента)
- атрибут класса students_count (количество учеников)
- атрибут экземпляра класса language (язык, которому обучается студент)
- атрибут экземпляра класса kpi (оценка студента)

Также класс должен содержать следующие методы:

- метод, который будет создавать нового ученика, и при этом увеличивать количество студентов на 1.
- метод который будет выводит имя и язык, выбранный учеником.
- а также метод, который будет устанавливать оценку ученику.
"""

"""
4) Dollar.
Создайте функцию dollarize, которая принимает дробное число (float) и переводит его в
долларизованный формат:

dollarize(123456.78901) -> "$123,456.80"
dollarize(-123456.7801) -> "-$123,456.78"
dollarize(1000000) -> "$1,000,000"

Создайте класс MoneyFmt, который содержит один единственный атрибут amount и 4 метода:
- init - инициализирует значение атрибута amount
- update - задаёт объекту новое значение amount
- repr - возвращает значение float
- str - метод, который реализует логику функции dollarize()

//Вывод должен выглядеть следующим образом:
cash = MoneyFmt(12345678.021)
print(cash) -- выводит "$12,345,678.02"
cash.update(100000.4567)
print(cash) -- выводит "$100,000.46"
cash.update(-0.3)
print(cash) -- выводит "-$0.30"
repr(cash) -- выводит -0.3
"""