# # ЗАДАЧА 1
# #
# # Реализовать класс Person, у которого должно быть два публичных поля: age и name.
# # Также у него должен быть следующий набор методов: know(person),
# #    который позволяет добавить другого человека в список знакомых.
# # И метод is_known(person), который возвращает знакомы ли два человека
#
#
# class Person(object):
#
#     def __init__(self,age,name):
#         self.age=age
#         self.name=name
#         self.lst_knows = []
#
#
#
#     def know_add(self,person):
#
#         if person in self.lst_knows:
#             print('{} уже знает по имени {}'.format(self.name,person))
#         else:
#             self.lst_knows.append(person)
#             print(self.lst_knows)
#
#
#     def is_know(self,person):
#
#         knowing_state=person in self.lst_knows
#         if knowing_state:
#             print('{} знаком с {}'.format(self.name,person))
#         else:
#             print('{} Не знаком с {}'.format(self.name, person))
#
#
# p=Person(14,'Misha')
# p.know_add('Misha')
# p.know_add('Саша')
# p.know_add('Джон')
# p.know_add('Саша')
# p.is_know('Джон')
#
#
# # ЗАДАЧА 2
# #
# # Есть класс, который выводит информацию в консоль: Printer,
# # у него есть метод: log(*values).
# # Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *
#
# class Printer(object):
#     def log(self,*values):
#         p=values
#         print(*p)
#
# class FormattedPrinter(Printer):
#
#     def format_print(self,*values):
#         v=values
#         for val in v:
#             print('*'*10)
#             self.log(val)
#             print('*' * 10)
#
#
#
#
# p=Printer()
# #p.log(10,33,15,66,'john','alisa')
#
# f=FormattedPrinter()
# f.format_print(10,33,15,66,'john','alisa')
#







# ЗАДАЧА 3
#
# Написать класс Animal и Human,
# сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
# Другие - нет. За что будет отвечать метод is_dangerous(animal)

# Слегка дополнил задачу:
# Человек наследуется от животного.
# И у животных и у людей добавлен параметр агрессии.
# У животного и у человека есть метод Атаковать человека.
# Если параметр агрессии у нападающего и жертвы совпадает считается,
# что жертва отбилась и не считает нападавшего опасным.
# В противном случае жертва добавляет нападающего в перечень опасных для себя существ

import random



class Animal(object):

    def __init__(self,aggressive,type,power):
        self.aggressive =aggressive
        self.type=type
        self.power=power


    def attak_power(self):
        power_animal = self.aggressive*self.power
        print('Power of {} is {}'.format(self.type,power_animal))
        return power_animal




class Attak(object):
    def __init__(self,animalOne_pow,animalTwo_pow):
        self.animal_one_k=animalOne_pow
        self.animal_two_k=animalTwo_pow
        self.result_list=[]


    def attak(self):

        result_attak=self.attak_result()
        self.print_result_attak(result_attak)

        return result_attak

    def attak_result(self):

        attak_result=self.animal_one_k*self.luck() - self.animal_two_k*self.luck()
        if attak_result < 0:
            return 'Succes!'
        elif attak_result == 0:
            return 'Draw!'
        else:
            return 'Lose!'
    def print_result_attak(self,result_to_print):
        print('*' * 20)
        print('Attack was', result_to_print)
        print('*' * 20)
        pass
    def luck(self):
        luck = random.randint(1, 10)
        return luck


Human=Animal(5,'Human',3)
Wolf=Animal(7,'Wolf',2)
Horse=Animal(2,'Horse',4)
Crocodile = Animal(9,'Croco',3)
Gippo=Animal(7,'Gippo',10)
Yojick=Animal(1,'Yojick',1)

animal_list=[Horse,Wolf,Crocodile,Gippo,Yojick]
human_attak_power=Human.attak_power()
is_dangeros=[]
for animal in animal_list:
    animal_attak_power=animal.attak_power()
    battle = Attak(human_attak_power,animal_attak_power)
    table_result = []

    for i in range(10):

        table_result.append(battle.attak())


    if table_result.count('Succes!') >5:
        is_dangeros.append({animal.type:'Danger'})
    else:
        is_dangeros.append({animal.type: 'Nyasha'})

print(is_dangeros)