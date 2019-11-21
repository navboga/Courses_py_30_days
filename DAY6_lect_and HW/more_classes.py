class Test(object):
    pass

class Test1(Test):
    pass

class Test2(Test1):
    pass

Test2.value = 2


t2=Test2()
t22=Test2

print(t2.value)
print(dir(Test2))
print(Test2.mro())

print(t22.value)

print(t2.__class__)


class MathMath(object):
    exchange=22
    def curs(self,day):
        self.day_num=day
        #self.exchange=12
        print(self.exchange * self.day_num)
    @staticmethod # обьявляем метод статическим и теперь для работы ему не нужно принимать self, его можно выполнить без self-похоже на функцию вложенную в класс
    def zzzzz():
        print('some')


#MathMath.exchange=100

m= MathMath()
m.exchange=9

result = m.curs(10)

m.zzzzz()