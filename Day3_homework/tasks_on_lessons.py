import random
#Написать функцию которая выбрасывает одно из 3х исключений TypeError,ValueError или RuntimeError
#в месте вызова функции обрабатывать все 3 исключения.

def exception_err():
    random_key = random.randint(1,3)
#except_dict ={1:TypeError, 2:ValueError, 3:RuntimeError}
    if random_key == 1:
        raise TypeError
    elif random_key == 2:
        raise ValueError
    elif random_key == 3:
        raise RuntimeError
#ловим несколько типов ошибок в зависимости какая будет вызвана

try:
    exception_err()
except TypeError:
    print('very starnge TypeError!!!')
except ValueError:
    print('very starnge ValueError!!!')
except RuntimeError:
    print('very starnge RuntimeError!!!')
else:
    print('its OK')

#Написать функц которая принимает на вход список, если все объекты в списке int - сортирует его иначе выбрасывает
#ValueError

def input_list(lst=None):
    print(type(lst),print(lst))
    if isinstance(lst,list):
        for i in lst:
            if not isinstance(i,int):
                raise ValueError
        lst.sort()
        return lst
    else:
        raise TypeError
try:
   print(input_list([6 ,12 ,'4',99,14,60,28]),'Отсортированный список')
except ValueError:
    print('In list not only int')
except TypeError:
    print('the input filed is not a list')





#Написать функцию которая принимает словарь,преобразует все ключи словаря к строкам и возвращает новый словарь

def dict_to_str(dct={}):
    new_dct={}
    for keys,value in dct.items():

        new_dct[str(keys)]=value
    return new_dct
a={4:'Vives', 8:'Car', 12:'Volvo', 'best_car':'Citroen'}
print(dict_to_str(a))

# написать функцию которая принимает список чисеk и возвращает их произведение.
def multiplay(*numbers):
    multiplay_digit = 1
    for number in numbers:
        multiplay_digit*=number
    return multiplay_digit
print(multiplay(10, 3 ,4))


