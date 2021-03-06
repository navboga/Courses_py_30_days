# Полиморфизм позволяет использовать функции по разному,
# вне зависимости от типа их параметров
# Возможность использовать функции по разному в зависимости
# от входных аргументов.
# Python динамическая типизация
# Утиная типизация -Если что то выглядит как утка, крякает как утка это скорее всего утка
# но мы не можем однозначно утвержать утка ли это.

# В PY Нет разницы какую функцию или метод класса вызывать , главное что бы у нее или у класса был нужный метод
# а следить за верно переданными данными задача разраработчика, что бы например в метод len()
# передавалось то от чего можно взять длину, или метод append применялся к списку, а не числу например,
# т.к изменить число методом append нельзя.

#например функция

def sum_two_object(one,two):
    return one + two
# в нее можно передать любые типы того что можно складывать, строки, списки, числа, кортежи..
# утиная типизация - если вы знаете что это можно складывать то это можно складывать и не важно какого это типа
# одну и ту же функцию мы можем использовать по разному, когда мы складываем числа мы производим математическую
#операцию, когда мы складываем строки мы производим конкатенацию,
# когда мы складываем кортежи мы выполняем слияние множеств.





#пример от лектора

# -*- coding: utf-8 -*-


class Parent(object):
    def call(self):
        print('Parent')


class Child(Parent):
    def call(self):
        print('Child')


class Example(object):
    def call(self):
        print('Ex')


def call_obj(obj):
    obj.call()


call_obj(Child())
call_obj(Parent())
