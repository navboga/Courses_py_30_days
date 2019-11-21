# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import inspect
import json

# import custom_exceptions
from custom_exceptions import UserExitException
from models import BaseItem
from utils import get_input_function

__author__ = 'sobolevn'


class BaseCommand(object):

    done_dict={}
    undone_dict={}
    @staticmethod
    def label():
        raise NotImplemented()

    def perform(self, objects, *args, **kwargs):
        raise NotImplemented()


class ListCommand(BaseCommand):
    @staticmethod
    def label():
        return 'list'

    def perform(self, objects, *args, **kwargs):

        if len(objects) == 0:
            print('There are no items in storage.')
            return

        for index, obj in enumerate(objects):
            print('{}: {}'.format(index, str(obj)))


class NewCommand(BaseCommand):
    @staticmethod
    def label():
        return 'new'

    @staticmethod
    def _load_item_classes():
        # Dynamic load:
        # def class_filter(klass):
        #     return inspect.isclass(klass) \
        #            and klass.__module__ == BaseItem.__module__ \
        #            and issubclass(klass, BaseItem) \
        #            and klass is not BaseItem

        # classes = inspect.getmembers(
        #         sys.modules[BaseItem.__module__],
        #         class_filter,
        # )
        # return dict(classes)

        from models import ToDoItem, ToBuyItem, ToReadItem

        return {
            'ToDoItem': ToDoItem,
            'ToBuyItem': ToBuyItem,
            'ToReadItem': ToReadItem,
        }

    def perform(self, objects, *args, **kwargs):
        classes = self._load_item_classes()  # переменной classes присваиваем значение-словарь из return(словарь) функций_load_item_classes

        print('Select item type:')
        for index, name in enumerate(classes.keys()):  # итерируемся по ключам печатаем значения индекс и ключ
            print('{}: {}'.format(index, name))

        input_function = get_input_function()  # присваиваем переменной вызов функции ввода пользователем
        selection = None
        selected_key = None

        while True:
            try:
                selection = int(input_function('Input number: '))  # получаем выбор пользователя ToDoItem, ToBuyItem, ToReadItem
                selected_key = list(classes.keys())[selection]  # создаем список по значению ключа выбранного пользователем

                break
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')

        selected_class = classes[selected_key]  # присваиваем по ключю переменной selected_class нужный класс(ToDoItem, ToBuyItem, ToReadItem) из импортированного класса classes
        print('Selected: {}'.format(selected_class.__name__))
        print()

        new_object = selected_class.construct() #вызываем метод construct из выбранного пользователем(ToDoItem, ToBuyItem, ToReadItem) класса classes, присваиваем return этого метода переменной

        objects.append(new_object) # добавляем в список objects резульатат вызова метода construct одного из классов (ToDoItem, ToBuyItem, ToReadItem)
        print('Added {}'.format(str(new_object))) # печатаем резульатат вызова метода construct одного из классов (ToDoItem, ToBuyItem, ToReadItem)
        print()
        return new_object # возвращаем резульатат вызова метода construct одного из классов (ToDoItem, ToBuyItem, ToReadItem)


class ExitCommand(BaseCommand):
    @staticmethod
    def label():
        return 'exit'

    def perform(self, objects, *args, **kwargs):
        raise UserExitException('See you next time!')



class DoneCommand(BaseCommand):
    @staticmethod
    def label():
        return 'done'

    def perform(self, objects, *args, **kwargs):


        if len(self.done_dict) >=1:
            print('Task list:')
            for key, item in self.done_dict.items():
                print(key, item)



        if len(objects) == 0:
            print('There are no items in storage.')
            return



        for index, obj in enumerate(objects):

            print('{}: {}'.format(index, str(obj)))
        im_f = int(input('input task number :'))

        try:

             self.done_dict[objects[im_f]]= 'Done'
             for key, item in self.done_dict.items():
                 print(key,item)

        except NameError:
             self.done_dict={}
             self.done_dict[objects[im_f]]= 'Done'
             for key, item in self.done_dict.items():
                 print(key, item)





class UndoneCommand(BaseCommand):
    @staticmethod
    def label():
        return 'undone'

    def perform(self, objects, *args, **kwargs):

        if len(self.done_dict) >= 1:
            print('Task list:')
            for key, item in self.undone_dict.items():
                print(key, item)

        if len(objects) == 0:
            print('There are no items in storage.')
            return

        for index, obj in enumerate(objects):
            print('{}: {}'.format(index, str(obj)))
        im_ud = int(input('input task number :'))

        try:
            if objects[im_ud] in self.done_dict:
                print('Task {} in DONE list!!!'.format(objects[im_ud]))
                print('Try mark another task')
                return
            self.undone_dict[objects[im_ud]] = 'Undone'
            for key, item in self.undone_dict.items():
                print(key, item)

        except NameError:
            self.undone_dict = {}
            self.undone_dict[objects[im_ud]] = 'Undone'
            for key, item in self.undone_dict.items():
                print(key, item)

