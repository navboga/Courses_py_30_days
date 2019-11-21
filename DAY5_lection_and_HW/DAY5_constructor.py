#create constructor

class Constructor_Test:
    def __init__(self):
        print('Constror called')
        print('Self is the object itself!',self)
t=Constructor_Test()
t1=Constructor_Test()
print('**************************')

class Car:
    def __init__(self):
        self.color = 'red'

c=Car()
c1=Car()
print()
print(c.color)
print('*___________*')
print(c1)

print('*____________*')


#Создадим новый конструктор для машин, будем передавать в него цвет и максимальную скорость.
class NewCar:
    engeen = 'V8-Turbo'
    def __init__(self,intresing_color,max_speed):
        self.color = intresing_color
        self.max_speed = max_speed

c2=NewCar('green',260)
c3=NewCar('yellow',180)
print()
print(c2.color,c2.max_speed,c2.engeen)
print('*___________*')
print(c3.color,c3.max_speed,c3.engeen)


# Этот конструктор получает переменные но не сохраняет значение , после print сборщик мусора чистит
class Table:
    def __init__(self,numb_of_legs_table):
        print('New table has {} legs'.format(numb_of_legs_table))

t=Table(4)
t1=Table(3)

print('**********************')
#Этот конструктор сохраняет переменную и мы можем к ней в дальнейшем обратиться

class Chair:
    def __init__(self,numb_of_legs,color):
        self.cnt_legs=numb_of_legs
        self.color=color

c=Chair(4,'Green')
print(c, c.cnt_legs,c.color)
print()
c1=Chair(3,'Red')
print('variable c did not change',c1.color,c.color,c1.cnt_legs,c.cnt_legs)
