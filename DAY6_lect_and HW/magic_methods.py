"""
Магические методы и магические константы
описание поискать в Google можно all magic methods


например
__init__ инициализация класса
__mro__ метод резолюшн ордер (наследование)
метод (str)
метод __add__

Для самостоятельного изучения
методы для работы с индексированием, слайсами последовательностями
методы используемые для создания и вызова обьектов
методы для работы с атрибутами класоов
другие.
6 лекц тайм метк 1час 5 мин

"""
#никакой практической нужности в следующем классе просто метод add что то к чему то пытается добавить
class BadStr(str):
    def __add__(self, other):
        return str(self) + str(other)

t = BadStr('some')
print( t + 2)

# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


class MathObject(object):
    def __init__(self, value):
        self.value = value

    # Comparing:
    def __eq__(self, other):
        return self.value == other

    def __ge__(self, other):
        return self.value >= other

    def __gt__(self, other):
        return self.value > other

    def __lt__(self, other):
        return self.value < other

    # Operations:
    def __neg__(self):
        return -self.value

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        return self.value ** other #переопределями работу магического метода mul- мультипликация- умножение, теперь он возвращает степень

    # def __mul__(self, other):
    #     return self.value * other # не переопределенный выглядит так.
    #     умножает 2 числа, то которое передано в создании экземлпяра класса MathObject(10.)
    #     и то которое передается вторым (other) в print(m + 3) или например в присвоении переменной
    #     в данном случае other=3 вклассическом определении
    #     выполнится магический метод __add__ который сложит m self.value в данном случая 10.
    #     и other=3, но если метод переопределить, например вместо return self.value + other
    #     написать return self.value * other то при вызове
    #     m=MathObject(10.)
    #     print(m + 3) произойдет умножение 10 на 3 хотя и было написано в print +
    #     таким образом мы переопределии дейстие метода класаа __add__ со сложения на умножение

if __name__ == '__main__':
    m = MathObject(10.)
    print(type(m))
    print(m > 10)
    print(m >= 10)
    print(m == 10)

    print(-m)
    print(m + 2 == 2 + m)

    m += 5 #тут m становится обьектом класса float
    print(type(m))
    print(m)
    print(m * 2)
    print('*'*8)
    print(m * 10)
    m = MathObject(10.)
    print(m * 10)
print('*'*8)

print (m.__dict__) # показывает внутренние состояние класса- всех переменных
print('*'*8)

print (m.__dir__()) #показывает все доступные методы объекта.