import random
#создадим список из N произвольных чисел и отсортируем в обратном порядке

lst=[8,22,5,16,99,14]
lst=sorted(lst,reverse=True)
print(lst)

# Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно
new_dct={1:'Yanv',2:'Feb',3:'Mart',4:'Apr',5:'May',6:'Jun'}

for key,val in new_dct.items():
    print(key,val)

# Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем
list_float=[]

for digit in range(10):
    list_float.append(round((random.uniform(1,10)),2))
tuple_float = tuple(list_float)

print('Создали кортеж со значениями {} и max:{}, и min:{}'.format(tuple_float,max(tuple_float),min(tuple_float)))

# Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,
# чтобы получилось: 'Earth -> Russia -> Moscow'
words_list=['Earth', 'Russia', 'Moscow']
print(' -> '.join(words_list))

# Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
URI_bin = '/bin:/usr/bin:/usr/local/bin'
print(URI_bin.split(':'))

# Пройти по всем числам от 1 до 100, написать в консоль,
# какие из них делятся на 7, а какие - нет
for i in range(1,15):
    if i % 7 == 0:
        print('{}- Делится на 7'.format(i))
    else:
        print('{}- Не делится на 7'.format(i))


# Создать матрицу любых чисел 3 на 4,
# сначала вывести все строки, потом все столбцы
#matrix_list = list([input().split()] for i in range(4))

#[print(*matrix_list[x]) for x in range(len(matrix_list))]

matrix_list1=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

for x in matrix_list1:
    print(*x )

for i in range(3):
     for x in range(4):
         print(matrix_list1[x][i])


# Создать список любых объектов, в цикле напечатать в консоль:
# объект и его индекс
new_list=[15,'Word', None, [1, 2, 3], False]
for z in range(len(new_list)):
    print('{} : {}'.format(z, new_list[z]))




# Создать список с тремя значениями
# 'to-delete' и нескольми любыми другими,
# удалить из него все значения 'to-delete'

delete_list=['to_delete', 17, 'to_delete', 'save', 'to_delete',23 ,99 ,'to_delete', 'good_boy']

for value in delete_list:
    if value == 'to_delete':
        delete_list.remove(value)
print(*delete_list)



# Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1),
# напечатать их в консоль
# Дополнительное задание:
# Для тех, кто решил игру загадки без использования циклов и словарей - прошу ради интереса сделать со словарем и циклом,
# посмотрите, насколько удобнее и короче стал ваш код.

