#работа с кортежем (tuple)
#кортеж не изменяем но расширяем т.е уже содержащиеся данные в кортеже не могут быть изменены, но можно выполнить слияние с другим кортежем (переприсвоить значение переменной содержащей
# кортеж сумме двух и более кортежей)
#кортеж может содержать одновременно любые типы данных и строку и число и None и bool

tuple1=(1,2,3,4,5)
print(tuple1)
tuple1=tuple1+(6, )# переприсвоили значение
tuple1+=(7, )

print(tuple1)
tuple1+=(8, )
print(tuple1)

tuple_text=('mother','wosh','the ramma','the end')
print(tuple_text[0],tuple_text[0:2],tuple_text[:-1],tuple_text[::],tuple_text[::-1])

###############################################################################################
"""
dict -словарь, не может использовать в качестве ключа изменяемые типы данных(list,dict), все остальное может вт ч None, число, кортеж.
в качестве значения могут быть использованы любые типы
"""