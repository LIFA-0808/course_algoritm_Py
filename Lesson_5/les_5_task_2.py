# Написать программу сложения или умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в
# несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных
# функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
from collections import deque


def redirect_num(num):
    for i, item in enumerate(num):
        if item in '0123456789':
            num[i] = int(item)
        elif item in h_nums:
            num[i] = h_nums[item]
    return num


def h_addition(num_1, num_2):
    deq_1 = deque(num_1)
    deq_2 = deque(num_2)
    len_1 = len(num_1)
    len_2 = len(num_2)
    max_len = max(len_1, len_2)
    # Приведение к одинаковому числу элементов
    if len_1 > len_2:
        deq_2.extendleft([0]*(len_1 - len_2 + 1))
        deq_1.appendleft(0)
    elif len_2 > len_1:
        deq_1.extendleft([0]*(len_2 - len_1 + 1))
        deq_2.appendleft(0)
    # Сложение
    temp_list = []
    for i in range(max_len):
        temp_list.append(deq_1.pop() + deq_2.pop())
    return temp_list


def hex_rendering(temp):
    # Функция приводящая ответ в шестнадцатиричное представление
    for i, item in enumerate(temp):
        if item > 15:
            temp[i] = item - 16
            temp[i+1] += 1
    result = []
    nums = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    for i in range(len(temp)):
        t = temp.pop()
        if t > 9:
            result.append(nums[t])
        else:
            result.append(t)
    return result


first = list(input('Введите первое число: ').upper())
second = list(input('Введите второе число: ').upper())

h_nums = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


first = redirect_num(first)
second = redirect_num(second)
answ = h_addition(first, second)

print(hex_rendering(answ))

