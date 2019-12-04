import time,datetime

# создаем функцию печати длительности выполнения готовой бибилиотеки time


def work_time():

    time_start=time.process_time()
    print(time_start)

# создаем функцию печати текущего времени из готовой бибилиотеки time


def sysdate():
    now=datetime.datetime.now()
    print(now)


# создаем декаратор для функции который печатает время
# начала выполнения,саму функцию, сколько выполнялась и время окончания
def decorator_stars(func):
    def inner(count):
        sysdate()
        func(count)
        work_time()
        sysdate()
    return inner

# применяем декаратор к функции печатающей плюсики
@decorator_stars
def print_plus(count):
    for i in range(count):
        print('+' * count)


print_plus(10)


print(dir(time))