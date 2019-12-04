#HW
"""
1 - Наприсать генератор который каждый раз возвращал бы новое случайное значение
2 - написать генератор который бы работал как range()
3 - написать генератор который бы работал как map()
4 - написать генератор который бы работал как enumerate()
5- написать генератор который бы работал как zip ()
"""
#1 - Наприсать генератор который каждый раз возвращал бы новое случайное значение

from random import randint


def random_dig():
    while True:
        yield randint(1,100)

randomise=random_dig()

print(next(randomise))
#2 - написать генератор который бы работал как range()

def rnge(start=0,stop=0,step=1):
  if start < stop:

    while start<stop:
        yield start
        start+=step

  if start > stop:

    while start >stop:
        yield start
        start+=abs(step) * -1

like_range=rnge(3,7)

try:
    for i in range(10):
        print(next(like_range))
except StopIteration:
    print('End of sequence')

#3 - написать генератор который бы работал как map()


numbers=['11','21','23','40']
funct = int
def new_map(function,lst:list):

    list_generate=iter(lst)

    value=next(list_generate)
    while True:
        yield function(value)
        value = next(list_generate)



nm=new_map(funct,numbers)
print(next(nm)+ next(nm) + next(nm))

#4 - написать генератор который бы работал как enumerate()
from pprint import pprint

def new_enumerate(some_iterable):
    a = 0

    iter_for_some_iterable=iter(some_iterable)

    while True:
        yield a, next(iter_for_some_iterable)
        a+=1

obj=['book',2,['some1','some2','some3']]
new_enum=new_enumerate(obj)

for i in range(len(obj)):
    print(*next(new_enum))

#5- написать генератор который бы работал как zip ()
print('*'*5,'5'* 10,'*'*5)
a = [1, 2, 3]
b = "xyz"

def new_zip(first_args,second_args):
    fst_args=iter(first_args)
    scd_args=iter(second_args)
    while True:
        yield next(fst_args),next(scd_args)

zip_result=new_zip(a,b)

for i in range(3):
    print(*next(zip_result))









