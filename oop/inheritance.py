"Наследование - принцип ООП, где мы можем в дочерном классе, унаследовать, переопределять и использовать  все аттрибуты и методы родительского класса"

class A:
    def method(self):
        print("method in class A")

obj_a = A()
obj_a.method() # "method in class A"

class B(A):
    """Наследовали все методы и аттрибуты у класса А"""

obj_b = B()
obj_b.method()# "method in class A"
"class A - Родительский класс"
"сlass B - дочерний класс"

class C(A):
    def method(self):
        print("method in class C")

obj_a = A()
obj_a.method() # "method in class A"

obj_c= C()
obj_c.method() # "method in class C"

"переопределение  - даем то же название, но другое значение"
"super() - функция которая позволяет обратиться к родительскому классу и вызвать определенные методы или аттрибуты"
class A:
    def range(self, n):
        return list(range(0, n+1))

class B(A):
    def range(self):
        return super().range(10)


"===========Виды наследования=============="
# одиночное наследование
# множественное наследование
# многоуровневое наследование
# иерархическое наследование
# гибридное наследоование
