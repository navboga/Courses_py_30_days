#Обработка Ошибок
#Basic try/except

try:
    100/10
    10/0
except:
    print('Wow wow wow!!! Division by Zero')

print('Programm still work')

try:
    print(1/0)
except Exception: #it is almost the same as just 'except:'
    print('Wow wow wow!!! Division by Zero')

print("еще работает")

try:
    int('b')
except ValueError:
    print('Wrong data for int!!!')

print('И тут программа работает')

# try:
#     1/0
# except ValueError: #Ожидали ValueError получили ZeroDivisionError программа прекратила работу т.к ожидался другой тип ошибки на деление на 0
#     print('Error')
# print('А тут упала!!')

try:
    1/0
except ZeroDivisionError: #Ожидали ZeroDivision и получили ZeroDivisionError программа продолжила работу но кинула исключение 0
    print('Error')


#ловим несколько типов ошибок в зависимости какая будет вызвана
try:
    1/int(input())
except ZeroDivisionError:
    print( '/0')
except TypeError:
    print('Wrong Type input Data')
except ValueError:
    print('Wrong data, input is not Digit')


#Сохраняем сам текст ошибки в переменную
#отдельно обрабатываем переменную с ошибкой, можем кидать в лог файл например
try:
    1/ int(input())
except ValueError as shit_happend:
    print('Wrong data, input is not Digit')
    print(shit_happend)

#TypeError

try:
    3 /'asd'
except TypeError as TE:
    print(TE)