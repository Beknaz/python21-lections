# #task1

# data = input('Введите имя, фамилию и возраст через пробел:\n').split()
# name = data[0]
# last = data[1]
# yers = data[-1]
# name = name.lower().replace('a', '').title()
# last = '*'.join(list(last))
# print((name + last) * int(yers))

# # task2

# string = input('введите строку: ').lower()
# a = string.count('a')
# o = string.count('o')
# i = string.count('i')
# e = string.count('e')
# y = string.count('y')
# u = string.count('u')
# print(f'В вашей строке насчитано {a+o+i+e+y+u} гласных букв')

# #task3

# login = input('Введите ваш юзернейм одним словом: ')
# center = int(len(login)/2)
# login2 =login[:center] + '&' +login[center:] + '$'
# pasword = login2.swapcase()
# print(f'Вам сгенерирован пороль: {pasword}')


# name = input()
# last_name = input()
# age = input()
# city = input()
# print(f'Вас зовут {name} {last_name}, Ваш возраст: {age}, Вы проживаете в городе {city}')

# string = input()
# print(len(string) > 5)

#========3=======
# mark = int(input())
# if mark >= 90:
#     print('Отлично, ваша оценка 5!')
# elif mark >= 80:
#     print('Здоровоб ваша оценка 4!')
# elif mark >= 70:
#     print('Хорошо, ваша оценка 3!')
# elif mark >= 60:
#     print('Вам стоит подучить материал')
# else:
#     print('Вы не сдали экзамен')

#==========4======
# number = int(input('число: '))
# if number <= -1:
#     print('negative')
# elif number >= 1:
#     print('positive')
# elif number == 0:
#     print('zero')


# =========7=====
# x = 12
# y = 12
# z = 12
# if x == y and x == z:
#     print('3')
# elif x == y or x == z:
#     print('2')
# else:
#     print('0')



# x = int(input())
# y = int(input())
# if x%y == 0:
#     print(f'{x} делится на {y}')
#     print(f"Частное:", (x//y))
# else:
#     print(f'{x} не делится на {y}')
#     print(f"Частное:", (x//y))
#     print(f'Остаток:', (x%y))


# for i in range(1, 101):
#     if i%3 == 0 and i%5 == 0:
#         print('FizzBuzz')
#     elif i%3 == 0:
#         print('Fizz')
#     elif i%5 == 0:
#         print('buzz')
#     else:
#         print(i)

# year = int(input())
# if year%4 == 0 and year%100 > 0 or year%400 == 0:
#     print(f'YES')
# else:
#     print(NO)


# num = int(input())
# a = ord('a')
# z = ord('z')
# A = ord('A')
# Z = ord('Z')
# if a<=num<=z or A<=num<=Z:
#     print('Это буква', chr(num))
# else:
#     print('Это не буква а символ', chr(num))

# greeting = str(input())
# if greeting is str('Hi'):
#     print('Привет!')
# else:
#     print('NO')

# parol = str(input('Введите пароль: '))
# if parol.isalpha():
#     print('Ваш пароль должен хранить только числа')
# elif (not parol.isdigit() and not parol.isalpha()) and len(parol) < 8:
#     print('Ваш пароль должен хранить только числа \nВаш пароль должен содержать не менее 8 символов')
# elif len(parol) < 8:
#     print('Ваш пароль должен содержать не менее 8 символов')
# else:
#     print('Ваш пароль сохранен')

# a = input('Введите ваши балы через запятую:' ).split(',')
# x = ((int(a[0]) + int(a[1]) + int(a[2])) / 3)
# if x >= 69:
#     print(f'Вы допущены к экзаменам. Ваш средний балл составляет {x}')
# else:
#     print('Вы недопущены ')

# import random
# moi = input("Сделайте выбор — камень, ножницы или бумага: ")
# wariki = ["камень", "бумага", "ножницы"]
# komp = random.choice(wariki)
# print(f"\nВы выбрали {moi}, компьютер выбрал {komp}.\n")
# if moi == komp:
#     print(f"Оба пользователя выбрали {moi}. Ничья!!")
# elif moi == "камень":
#     if komp == "ножницы":
#         print("Камень бьет ножницы! Вы победили!")
#     else:
#         print("Бумага оборачивает камень! Вы проиграли.")
# elif moi == "бумага":
#     if komp == "камень":
#         print("Бумага оборачивает камень! Вы победили!")
#     else:
#         print("Ножницы режут бумагу! Вы проиграли.")
# elif moi == "ножницы":
#     if komp == "бумага":
#         print("Ножницы режут бумагу! Вы победили!")
#     else:
#         print("Камень бьет ножницы! Вы проиграли.")

# name_of_list = ['Beknaznazarbek']
# for n in name_of_list:
#     x = (len(n) // 2) + (len(n) % 2) 
#     new_list = n[x:] + n[:x]
#     print(list(new_list))

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = a.copy()
# for c in a.keys():
#     print(c)

#     for b in a.values():
#         if b % 2 == 0:
#             b = 2
#     print(c + b)

# task3 list
name_of_list = ['HelloWorld!']
a = int((len(name_of_list[0])) / 2)
if int(len(name_of_list[0])) % 2 != 0:
    a = int((len(name_of_list[0])) / 2) + 1
b = name_of_list[0][:a]
c = name_of_list[0][a:]
new_list = c + b
print(list(new_list))


# university = {'програмирование':25, 'экономика':30, 'медицина':40}
# university['програмирование'] = 20
# uni2 = {'лингвистика':50}
# university.update(uni2)
# university.pop('медицина')
# num = list(university.values())
# print((int(num[0])) + (int(num[1])) + (int(num[2])))



# y = {1: 'a', 2: 'b', 3: 'c'}
# b = list(y.values())
# c = list(y.keys())
# x = {b[0]:c[0], b[1]:c[1], b[2]:c[2]}
# print(x)

# number_of_guests = int(input('Количество гостей: '))
# guest_dictionary = {}
# for i in range(number_of_guests):
#   names = input('Введите имя гостя: ')
#   guest_dictionary[i+1] = names
# print(guest_dictionary)

# kolichestvo = int(input('kolichestvo:' ))
# spisok = {}
# for b in range(kolichestvo):
#     gosti = input('imena gostey poocheredno:' )
#     spisok[b+1] = gosti
# print(spisok)
    
# dictionary = {
#   "potato": 3,
#   "milk": 5,
#   "tomato": 4,
#   "carrot": 2
# }
# number_of_groceries = len(list(dictionary.keys()))
# print(dictionary)
# for i in range(number_of_groceries):
#   user_input = input()
#   dictionary.pop(f'{user_input}')
#   print(dictionary)

# list_ = range(54, 9184)
# list1 = []
# for b in list_:
#     if b % 5 == 0:
#         list1.append(b)
# print(list(list1))

# sum = 200
# while sum >= 0:
#     num = int(input())
#     sum = sum - num
#     if num > sum:
#         print('error')
#     else:
#         print('остаток:', sum)

"""
1) Дан список в котором хранится строка. Разрежьте его на две равные части (если длина строки нечетная, то длина первой части должна быть на один символ больше). Переставьте эти две части местами, при этом каждый символ должен являться отдельной строкой, результат запишите в новый список и выведите на экран.
"""
name_of_list = ['BeknazNazarbek']
a = int((len(name_of_list[0])) / 2)
if int(len(name_of_list[0])) % 2 != 0:
    a = int((len(name_of_list[0])) / 2) + 1
b = name_of_list[0][:a]
c = name_of_list[0][a:]
new_list = c + b
print(list(new_list))

"""
2) Дан список, состоящий ровно из двух строк. Переставьте эти слова местами. Результат запишите в список и выведите получившийся результат.
"""
list_ = ['asdf', 'asdfr']
list1 = list(list_.copy())
list1.reverse()
print(list1)
"""
3) Даны два множества. С помощью определенного метода (оператора) найдите пересечение множеств:
"""
a = {1, 2, 3, 4, 5, 6}  
b = {4, 3, 6 ,1, 8, 9}
print(a.intersection(b)) 
print(a & b)
"""
4) Четверо коллег собрались на обед. Но они не могут решить, где им пообедать, так как у каждого свои вкусовые предпочтения. Помогите найти им выход в данной ситуации. Данные:

-Тилек хочет покушать в Dodo или в ImperiaPizza, ну или в крайнем случае FreshBox.
-Тимур хочет покушать шашлык в OchakKebab или рамен в FreshBox.
-Александр очень хочет вафли с FreshBox либо KFC.
-Элину устраивает любой из вариантов. 

Напишите код, который сможет определить, в какое место им лучше пойти.
"""
Tilek = ['Dodo', 'ImperiaPizza', 'Freshbox']
Timur = ['OchakKebab', 'Freshbox']
Alex = ['Freshbox', 'KFC']
Elina= ['Freshbox', 'KFC', 'OchakKebab', 'ImperiaPizza', 'Dodo']
dict = {}
for i in Tilek:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for i in Timur:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for i in Alex:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for i in Elina:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(max(dict, key=dict.get))


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
"""
5) Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным.
"""
fruit = {'banan': 45, 'alma': 50, 'almurut': 61}
new_fruit = {k:v for k, v in fruit.items() if v % 2 != 0}
print(new_fruit)

"""
6) Создайте словарь, где значениями будут являться числа. Найдите сумму этих значений.
"""
a = {'b':5, 'a':10, 'c':4}
b = {v for v in a.values()}
print(int(sum(b)))
"""
7) Создайте словарь из чисел от 1 до 10, где ключами будут сами числа, а значениями их квадраты.
"""
a = {i:i ** 2 for i in range(1,11)}
print(a)
"""
8) Дан словарь, значениями в котором являются другие словари. Замените внутренние словари их значениями. Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}} -> {'first': 1, 'second': 2}
"""
my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
new_dict = {k:val for k, v in my_dict.items() for val in v.values()}
print(new_dict)
"""
9) Дан словарь. Попытайтесь получить значение по ключу. Обработайте ошибку, возникающую в том случае, если такого ключа нет.
"""
dict2 = {1:2, 3:453254, 5:64365}
a = int(input())
if a in dict2:
 print(dict2[a])
else:
 print('ключа', a, 'не существует')

# if dict2.get(a) == None:
#     print('Ключа', a, 'не существует')
# else:
#     print(dict2.get(a))


"""
10) Запросите у пользователя сумму, которая у него сейчас есть в бумажнике. Если он введёт сумму, меньшую чем 0, то выбросите исключение с текстом "Сумма не может быть отрицательной!"
"""
summa = int(input())
if summa < 0:
    print("Сумма не может быть отрицательной!")
else:
    print('У вас есть', summa, 'сомов')