"========переменные========"
# переменные    -   это ссылки на ячейки памяти, где храняться какие-то данные
a = 4
b = 4
"==========Ввод и вывод данных============"
# print - функция вывода данных в терминал
# input - функция ввода данных с терминала

b = input()
print("введенное число", a, b)

"========Числа========"
# integers(int) - целые числа (5, 10, -35, 0, 1)
a = 6
# float - вещественные (с плавающей точкой) (0.3, 0,345, 24.4543625 все что угодно с точкой)
b = 10.34
# decimal - точное вещественное число
# чтобы использовать десимал нужно его импортировать
from decimal import Decimal
c = Decimal(0.1)

# complex - комплексные числа
complex(1, 5)
"===========Операции над числами============="
5 + 5
10 - 3 
2 * 3
15 / 3 # деление (float 5.0всегда вещественные)
15 // 2 # целочисленное. сокращает в целое число 7
5 % 2 # остаток от деления (int 1)
5 ** 2 # возведение в степень
25 ** 0.5 # квадратный корень числа
 
 # модуль числа - из отрицательного числа сделает положительное |-5| = 5
 abs(-5) # 5
 abs(10) # 10
 abs(-2.4) # 2.4

 # pow:
 #1. возводит число в определенную степень 
 #2. возвращает остаток от деления результата 1 действия на третье число

 pow(2, 3) # 8 = 2 ** 3
 pow(2, 3, 4) # 8 % 4 = 0
 #  (2 ** 3) % 4 = 0

 # divmod - функция, которая принимает 2 числ и возвращает 2 числа, где первое - целая часть от деления, а второе это остаток
 divmod(15, 2)  # 7, 1
 divmod(9, 3)  # 3, 0
 # round - функция которая округляет число
 # sqrt - функция для нахождения корня числа
 # для работы нужно ее импортировать ищ библеотеки math 
 from math import sqrt