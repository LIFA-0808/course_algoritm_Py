# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в
# рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки)
# вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
# а проявили творчество, фантазию и создали универсальный код для замера памяти.

# Исходное задание: Определить, какое число в массиве встречается чаще всего.
'''В ходе анализа мной был выбран оптимальный вариант - var_two(size).

Оказалось, что использование tuple(в оптимольном варианте) заметно эффективнее, чем list(в базовом варианте)
и тем более set(в третьем варианте).'''
from random import randint
from sys import version, platform, getsizeof

print(version, platform)


# 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] win32


def show_size(x, level=0):
    size = 0
    print('\t' * level, f'type={x.__class__}, size={getsizeof(x)}, object={x}')
    size += getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'item'):
            for xx in x.items():
                show_size(xx, level + 1)
                size += getsizeof(xx)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)
                size += getsizeof(xx)
    return size


def size_def(func):
    memory_size = 0
    for i in func:
        show_size(i)
        memory_size += show_size(i)
    print(f'При вызове использовалось {memory_size} байт(-ов)')


def var_base(size):
    array = [randint(1, 10) for _ in range(size)]  # определяем случайный массив
    often_num = 0
    # print(f'array = {array}')

    results = [0 for _ in range(11)]  # находим сколько раз повторяются элементы
    for i in array:
        for num in range(11):
            if i == num:
                results[num] += 1
    # print(results)

    for i in results:  # определяем самый частый(-ые) элемент(ы) и выводим
        if i > often_num:
            often_num = i
    index_num = [i for i, x in enumerate(results) if x == often_num]
    # print(f'Чаще всего в массиве встречается {index_num}: {often_num} раз(-а)')
    return array, often_num, results, index_num


# size_def(var_base(10))
'''При вызове использовалось 606 байт(-ов)

type=<class 'list'>, size=100, object=[3, 4, 5, 1, 5, 1, 9, 2, 2, 9]
    type=<class 'int'>, size=14, object=3
    type=<class 'int'>, size=14, object=4
    type=<class 'int'>, size=14, object=5
    type=<class 'int'>, size=14, object=1
    type=<class 'int'>, size=14, object=5
    type=<class 'int'>, size=14, object=1
    type=<class 'int'>, size=14, object=9
    type=<class 'int'>, size=14, object=2
    type=<class 'int'>, size=14, object=2
    type=<class 'int'>, size=14, object=9

type=<class 'int'>, size=14, object=2

type=<class 'list'>, size=100, object=[0, 2, 2, 1, 1, 2, 0, 0, 0, 2, 0]
    type=<class 'int'>, size=12, object=0
    type=<class 'int'>, size=14, object=2
    type=<class 'int'>, size=14, object=2
    type=<class 'int'>, size=14, object=1
    type=<class 'int'>, size=14, object=1
    type=<class 'int'>, size=14, object=2
    type=<class 'int'>, size=12, object=0
    type=<class 'int'>, size=12, object=0
    type=<class 'int'>, size=12, object=0
    type=<class 'int'>, size=14, object=2
    type=<class 'int'>, size=12, object=0

type=<class 'list'>, size=52, object=[1, 2, 5, 9]
    type=<class 'int'>, size=14, object=1
    type=<class 'int'>, size=14, object=2
    type=<class 'int'>, size=14, object=5
    type=<class 'int'>, size=14, object=9'''


def var_two(size):
    array = tuple([randint(1, 10) for _ in range(size)])  # определяем случайный массив
    often_num = 0
    # print(f'array = {array}')

    results = [0 for _ in range(11)]  # находим сколько раз повторяются элементы
    for i in array:
        for num in range(11):
            if i == num:
                results[num] += 1
    # print(results)

    for i in results:  # определяем самый частый(-ые) элемент(ы) и выводим
        if i > often_num:
            often_num = i
    index_num = tuple([i for i, x in enumerate(results) if x == often_num])
    # print(f'Чаще всего в массиве встречается {index_num}: {often_num} раз(-а)')
    return array, often_num, results, index_num


# size_def(var_two(10))
'''При вызове использовалось 512 байт(-ов)

type=<class 'tuple'>, size=68, object=(5, 7, 9, 5, 9, 3, 5, 8, 10, 10)
     type=<class 'int'>, size=14, object=5
     type=<class 'int'>, size=14, object=7
     type=<class 'int'>, size=14, object=9
     type=<class 'int'>, size=14, object=5
     type=<class 'int'>, size=14, object=9
     type=<class 'int'>, size=14, object=3
     type=<class 'int'>, size=14, object=5
     type=<class 'int'>, size=14, object=8
     type=<class 'int'>, size=14, object=10
     type=<class 'int'>, size=14, object=10

type=<class 'int'>, size=14, object=3

type=<class 'list'>, size=100, object=[0, 0, 0, 1, 0, 3, 0, 1, 1, 2, 2]
     type=<class 'int'>, size=12, object=0
     type=<class 'int'>, size=12, object=0
     type=<class 'int'>, size=12, object=0
     type=<class 'int'>, size=14, object=1
     type=<class 'int'>, size=12, object=0
     type=<class 'int'>, size=14, object=3
     type=<class 'int'>, size=12, object=0
     type=<class 'int'>, size=14, object=1
     type=<class 'int'>, size=14, object=1
     type=<class 'int'>, size=14, object=2
     type=<class 'int'>, size=14, object=2

type=<class 'tuple'>, size=32, object=(5,)
     type=<class 'int'>, size=14, object=5'''


def var_three(size):
    array = [randint(1, 10) for _ in range(size)]  # определяем случайный массив
    often_num = 0
    # print(f'array = {array}')

    results = [0 for _ in range(11)]  # находим сколько раз повторяются элементы
    for i in array:
        for num in range(11):
            if i == num:
                results[num] += 1
    # print(results)

    for i in results:  # определяем самый частый(-ые) элемент(ы) и выводим
        if i > often_num:
            often_num = i
    index_num = set([i for i, x in enumerate(results) if x == often_num])
    # print(f'Чаще всего в массиве встречается {index_num}: {often_num} раз(-а)')
    return array, often_num, results, index_num


# size_def(var_three(10))
'''При вызове использовалось 640 байт(-ов)

type=<class 'list'>, size=100, object=[5, 6, 9, 5, 3, 5, 3, 4, 4, 4]
     type=<class 'int'>, size=14, object=5
     type=<class 'int'>, size=14, object=6
     type=<class 'int'>, size=14, object=9
     type=<class 'int'>, size=14, object=5
     type=<class 'int'>, size=14, object=3
     type=<class 'int'>, size=14, object=5
     type=<class 'int'>, size=14, object=3
     type=<class 'int'>, size=14, object=4
     type=<class 'int'>, size=14, object=4
     type=<class 'int'>, size=14, object=4

type=<class 'int'>, size=14, object=3

type=<class 'list'>, size=100, object=[0, 0, 0, 2, 3, 3, 1, 0, 0, 1, 0]
     type=<class 'int'>, size=12, object=0
     type=<class 'int'>, size=12, object=0
     type=<class 'int'>, size=12, object=0
     type=<class 'int'>, size=14, object=2
     type=<class 'int'>, size=14, object=3
     type=<class 'int'>, size=14, object=3
     type=<class 'int'>, size=14, object=1
     type=<class 'int'>, size=12, object=0
     type=<class 'int'>, size=12, object=0
     type=<class 'int'>, size=14, object=1
     type=<class 'int'>, size=12, object=0
     
type=<class 'set'>, size=116, object={4, 5}
     type=<class 'int'>, size=14, object=4
     type=<class 'int'>, size=14, object=5'''
