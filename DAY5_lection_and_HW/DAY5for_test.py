#Classes can have both methods and fields
class Window:
    is_opened = False
    cnt=3
    lst=[]

    def open(self):
        self.is_opened = not self.is_opened
        self.cnt+=10
        self.lst.append(self.cnt)
        print('Window is now', self.is_opened)

w = Window() # w Экземпляр класса Window
w1 = Window() #1 w Экземпляр класса Window

print('Initial state', w.is_opened,w.cnt,w1.is_opened)
for i in range (5):
    w.open()
    print('New state', w.is_opened,w.cnt,w1.is_opened,w.lst)
print(w.lst)
class Constructor_Test:
    def __init__(self):
        print('Constuctor called')
        print('Self is the object itself!',self)
t=Constructor_Test()
t1=Constructor_Test()
print('**************************')
# class Chair:
#     def __init__(self,numb_of_legs,color):
#         self.cnt_legs=numb_of_legs
#         self.color=color
#
# c=Chair(4,'Green')
# print(c, c.cnt_legs,c.color)
# print()
# c1=Chair(3,'Red')
# print('variable c did not change')
# print(c1.color)
# print(c1.cnt_legs)
# print(c.color)
# print(c.cnt_legs)