# class Car:
#     pass
# c=Car()
# print(c,type(c))
#
# class Room:
#     number = 'Room 34'
#     flor =4
#
# r=Room()
# r1=Room()
# print(r.number,r1.number)
# print(r.flor,r1.flor)
#
# #You can modify values:
# print('*_____________*')
# r.number=12
# r.flor='5 Flor'
#
# print(r.number,r1.number)
# print(r.flor,r1.flor)
# print('*_____________*')
# #Classes can have functions inside: its called method

class Dor:
    def open(self):
        print('self is:', self) #note that 'self' is the object
        print('Dor is opened')
        self.opened=True
z = Dor()
z1 =Dor()
z2=Dor()
z2.open()
print(z2,'!!!!!!!!!')
z2.open()
print(z2.open(),'**********')
z.open()# Method
z1.open()
z2.open()
print('!!!!!!!!!!!__________!!!!!!!!!!')
d=Dor().open()
print(z.opened)
print(z1)
print(z2.open())
print(z2.opened,z2)

# Method can accept params
print('*******************')
class Terminal:
    def hello(self,username):
        print('self is the object itself', self)
        print('Hello',username)

t = Terminal()
t.hello('Andrey')
t.hello('Maksim')
print('*******************')

#Classes can have both methods and fields
class Window:
    is_opened = False
    def open(self):
        self.is_opened = not self.is_opened
        print('Window is now', self.is_opened)

w = Window()# w Экземпляр класса Window
w1 = Window()

print('Initial state', w.is_opened,w1.is_opened)

w.open()
print('New state', w.is_opened,w1.is_opened)
