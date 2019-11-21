#продолжим примеры обработки ошибок

# try:
#     d={'key':23}
#     print(d['does not exist'])
# except ZeroDivisionError:
#     print("this won't be called")


#KeyError
try:
    d={'key':23}
    print(d['does not exist'])
except KeyError as k:
    print("Catch it",k)


#IndexError
print()
print()
try:
    lst=[1, 2, 3]
    print(lst[4])
except IndexError as ie:
    print('Превышен индекс элемента',ie)