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

sum = 200
while sum >= 0:
    num = int(input())
    sum = sum - num
    if num > sum:
        print('error')
    else:
        print('остаток:', sum)