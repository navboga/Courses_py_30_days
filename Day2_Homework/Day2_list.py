not_a_list=(1,3,5) #Создаем кортеж-коллекцию-tuple

list1=[2,4,6]
list2=[]
list3=[1,3,5]
list2=list(not_a_list)
print(list3==list2,list3+list1,list1+list2) #сравниваем, конкотинируем , конкотинируем.
list1.append(8) #добавляем в конец знчение 8
print(list1)
list1.insert(2,7)#расширяем список вставля на позицию следующую за индексом 2 значени 7 все элементы после сдвигаются на 1 позицию
print(list1)
list1.remove(7)#удаляем первую по списку семерку
print(list1)
list1.insert(3,7)# использовать insert не рекомендуется очень медленно, если приходится использовать инсерт, значит что то делаем не так
list1.append('BMW')
print(list1)
var=list1.index('BMW')#получаем индекс элемента 'BMW' и присваеваем значение переменной var
list1[var]='MERSEDES'#присваиваем новое значение элементу списка list1 с индексом = var
print(list1)

#delete
new_list=['pop','remove','del']
popped=new_list.pop(0)
print('popped value is {}.'.format(popped),new_list)

new_list.remove('remove')
print(new_list)

del new_list[0]
print(new_list)