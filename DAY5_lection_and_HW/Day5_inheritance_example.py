#создадим основной родительский класс Callc суммирующий 2 числа
class Callc(object):
     def __init__(self,number1,number2):
         self.num1=number1
         self.num2=number2

     def calc_and_print(self):
         summ=self.calc_value()
         self.print_result(summ)

     def calc_value(self):
         return self.num1 + self.num2

     def print_result(self,summ_to_print):
         print('*----------*')
         print('Result is', summ_to_print)
         print('*----------*')

c=Callc(4,5)
c.calc_and_print()

#Созададим класс потомок Callc вычитающий 2 числа

class Callc_minus(Callc):
    #определим в нем новые действия для метода calc_value
    def calc_value(self):
        return self.num1-self.num2
#привяжем класс к переменной delta

delta=Callc_minus(9,5)

delta.calc_and_print()

#Созададим класс потомок Callc умножающий 2 числа,переопределим в нем новые действия для метода calc_value, осталтные методы
#остануться доступны из родительского класса и будут выполняться в нем

class Callc_multiplication(Callc):
    def calc_value(self):
        return self.num1 * self.num2

#привяжем класс к переменной multi и выполним метод calc_and_print()

multi=Callc_multiplication(3,10)
multi.calc_and_print()

# или не привязывая выполним метод calc_and_print() класса Calc_multiplication являющегося потомком класа Callc
Callc_multiplication(10,10).calc_and_print()
