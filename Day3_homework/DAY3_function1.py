def sum_function(x, y):
    summ=x+y
    return 'Функция вернула сумму {} и {} равную {}'.format(x,y,summ)

print(sum_function(5,20))


def with_default(name='Chandler'):
    print('Привет', name)

with_default('Jenis')


# функция с неопределенным кол-вом позиционных(без значения по умолчанию) элементов.Например print() в который можено передать бесконечное множество эл-ов.
#создадим такую:

def many_args(*numbers): # *name -ожидает любое кол-во элементов на вход преобразуется в tuple- кортеж
    return (sum(numbers), type(numbers))
func_return=many_args(1, 2, 3, 4, 5, 6)
print(func_return[0],func_return)

#или просто
def many_args_print(*numbers): # *name -ожидает любое кол-во элементов на вход преобразуется в tuple- кортеж
    print(sum(numbers), type(numbers))
many_args_print(10, 20, 3, 40, 5, 6)


#любое кол-во keyword (со значением по умолчанию)
def any_keywords(**kwargs):
    print(kwargs,type(kwargs))

any_keywords(k1=80,drp='knehth', r2d2='warior', mast_have=1)

