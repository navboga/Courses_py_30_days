#super() позволяет обращаться(вызывать) к методам родителей
#упрощает переиспользование кода
# если потомок наследует все методы родителя и прародителей.
#если использовать super()...и у родителя нет метода
# будет обращение к прародителю и так по цепочке до верха в иерархии
#доклад https://www.youtube.com/watch?v=EiOglTERPEo


class Calc(object):
    def __init__(self,value):
        print('Calc constructor is called')
        self.value=value
    def calculate(self):
        return self.value * 2 * 5
c=Calc(10)
print(c.calculate())



class ExtendedCalc(Calc):
    def __init__(self,value, coef= 1.3):
        super().__init__(value)
        print ('ExtCalc constuctor and super(Calc) is called')
        self.coef=coef
    def new_calculate(self):
        previous=super().calculate() #вызываем метод родителя
        print(previous)
        return -1 * self.coef * previous
ec=ExtendedCalc(7,4)
print(ec.new_calculate())


print(*dir(ExtendedCalc), sep='\n')

print(ExtendedCalc.__mro__)