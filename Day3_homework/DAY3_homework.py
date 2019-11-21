# Задачи на закрепление типов аргументов:
# Написать функцию, которая принимает любое количество аргументов чисел.
# Среди них она находит максимальное и минимальное. И возвращает оба

def any_min_max(*digits):
    min_digit = min(digits)
    max_digit = max(digits)
    print(digits,type(digits))
    return min_digit ,max_digit
print('min {}, max {}'.format(any_min_max(1, 100, 500, 38 ,66, 14, 0.16, 222222 )[0],any_min_max(1, 100, 500, 38 ,66, 14, 0.16, 222222 )[1]))



# Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True.
# Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, иначе - к нижнему

def UPandDOWN(string:str,bool_tipe:bool):
    if bool_tipe:
        new_string=string.upper()
        return new_string
    else:
        new_string=string.lower()
        return new_string
print(UPandDOWN('Мама мыла Раму',True))






# Написать функцию, которая принимает любое количество позиционных аргументов - строк
# и один парматер по-умолчанию glue, который равен ':'.
# Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов.
# Для соединения между любых двух строк вставлять glue

def concat_string(*str, glue=':'):
    new_str=''
    for s in str:
        if len(s) >3:
            if len(new_str)>0:
                new_str +=glue + s
            else:
                new_str +=s
    return (new_str)
print(concat_string('BMW','Mersedes','VAZ','UAZ','JEEP','MITSUBISI','Kia','Citroen'))