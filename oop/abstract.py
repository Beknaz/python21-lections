"====================Абстракция=================="
# абстракция - принцип ООП, в котором создается абстрактный класс(класс пустышка), в котором задаются названия аттрибутов и методов для того, чтобы в дочерних классах переопределить их нужным. образом от абстрактный классов мы не создаем обьектов, потому что в них есть только названия и нет логики

from abc import ABC, abstractclassmethod, abstractproperty

class AbstracrAnimal(ABC):
    @abstractclassmethod
    def voice(self):
        ...
    
    @abstractproperty
    def legs(self):
        ...

obj = AbstracrAnimal