"""
Переиспользование кода из файла
Любой Python -файл -МОДУЛЬ,
папка с модулямя и ФАЙЛОМ __init__.py -ПАКЕТ

sys.path -хранит пути по которым лежай пайтоновские модули. и при импорте нужный модуль ищется по этим путям.

C:\\Users\\akrylov\\pyt\\Day2_Homework\\venv\\lib\\site-packages\\pip-10.0.1-py3.7.egg - это установленные пакеты
"""
import sys

print(sys.path)

"""
Пример: Импортируем из пакета normal_package(потому что в папке есть __init_.py модуль )
модуль normal_file
при этом в импортируемом модуле normal_file желательно присутсвие записи:
if __name__ == '__main__':
    my_function()
тк при импорте интерпритатор python выполняет все что есть в импортируемом файле,
и присутствие вышеуказанной конструкции не даст функции my_function() выполнится
при импорте, т.к магический метод __name__ (показывает отуда происходит вызов файла иначе говоря выполнение программы),
равен строке '__main__'(главный основной) только если
вызов проиходит из самого себя файла (например normal_file.py) приимпорте же
вызов приоиходит из удаеленного файла поэтому внутренний __name__ не равен '__main__'


"""
# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


from normal_package.normal_file import MyClass, my_function, GLOBAL_VAR

my_function()


try:
    from not_a_package.my_module import print_info

    # why does it happen:
    # http://stackoverflow.com/questions/16981921/relative-imports-in-python-3
    print_info()
except ImportError as e:
    print(e)
