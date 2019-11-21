#выбрасываем ошибку наружу -ключевое слово raise

#raise IndexError ('Hi!!!') # после наступления raise выбрасывается ошибка и работа программы завершается.

#raise ValueError('F1')

#перехватываем собственную ошибку

try:
    raise KeyError('Very bad Boy!!!')
except KeyError as ke:
    print('I fix it later', ke)


# примеры с блоком else try/except/else
#блок else сработает если нет ошибки
try:
    print('All fine!!!')
except KeyError:
    print('vary strange')
else:
    print('No worning!')

# try/except/finaly
#,блок finaly сработает всегда
try:
    1/0
except ZeroDivisionError as ze:
    print('/0')
finally:
    print('I will be called in the end')

# All together
print()
print() #пропустим две строки для удобства чтения


try:
    print('try')
except TypeError:
    pass #просто пропуск Никогда не нужно игнорировать ошибки
else:
    print('else')
finally:
    print("it's all about exception" )


try:
    raise ValueError('like catched exception')
finally:
    print('finally всегда работает, даже после raise')

