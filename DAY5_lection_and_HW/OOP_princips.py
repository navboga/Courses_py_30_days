#Основные приниципы ООП
#Наследование-посзволяет переиспользовать тот код, который у вас уже есть, что делает разработку быстрее inheritance. Все python обьекты наследуются от object!!
#Инкапсуляция
#Полиморфизм
#Абстракция-? в некоторых случаях


#inheritance
# -*- coding: utf-8 -*-


class Parent(object):
    def __init__(self):
        print('Parent inited')
        self.value = 'Parent'

    def do(self):
        print('Parent do(): %s' % self.value)


class Child(Parent):
    def __init__(self):
        print('Child inited')
        self.value = 'Child'


parent = Parent()
parent.do()

child = Child()
child.do()
