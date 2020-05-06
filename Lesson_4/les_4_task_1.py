# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
# первых трех уроков. Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом
# (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

# Исходное задание: В диапазоне натуральных чисел от 2 до n определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
""" В ходе анализа 3-х реализаций функиции был сделан вывод, что функция composite_2 - является оптимальным решением,

так как функция выполняется за константное время и в её реализации не была использована рекурсия, что позволяет
работать с большими значениями."""
import cProfile


def test_composite(func):
    ex_result = [49, 33, 24, 19, 16, 14, 12, 11]
    n = 99
    assert func(n) == ex_result
    print(f'Test is OK')


def composite(n):
    result = [0, ]*8
    for item in range(2, n+1):
        for num in range(2, 10):
            if item % num == 0:
                result[num - 2] += 1
    return result


# test_composite(composite)

# cProfile.run('composite(100)')
# 4 function calls in 0.000 seconds

# cProfile.run('composite(200)')
# 4 function calls in 0.000 seconds


# "les_4_task_1.composite(100)"
# 1000 loops, best of 5: 89.8 usec per loop

# "les_4_task_1.composite(200)"
# # 1000 loops, best of 5: 181 usec per loop

# "les_4_task_1.composite(500)"
# 1000 loops, best of 5: 449 usec per loop

# "les_4_task_1.composite(1000)"
# 1000 loops, best of 5: 937 usec per loop

# "les_4_task_1.composite(10000)"
# 1000 loops, best of 5: 9.37 msec per loop

# "les_4_task_1.composite(50000)"
# 1000 loops, best of 5: 53.9 msec per loop


def composite_2(n):
    result_2 = [n//2, n//3, n//4, n//5, n//6, n//7, n//8, n//9]
    return result_2


# test_composite(composite_2)

# cProfile.run('composite_2(100)')
# 4 function calls in 0.000 seconds

# cProfile.run('composite_2(10000)')
# 4 function calls in 0.000 seconds

# "les_4_task_1.composite_2(100)"
# 1000 loops, best of 5: 1.08 usec per loop

# "les_4_task_1.composite_2(10000)"
# 1000 loops, best of 5: 1.17 usec per loop

# "les_4_task_1.composite_2(50000)"
# 1000 loops, best of 5: 3.03 usec per loop

result_3 = [0, ]*8


def composite_3(n):
    if n == 2:
        result_3[0] += 1
        return result_3
    else:
        for num in range(2, 10):
            if n % num == 0:
                result_3[num-2] += 1
        n -= 1
        return composite_3(n)


# test_composite(composite_3)

# cProfile.run('composite_3(100)')
# 102 function calls (4 primitive calls) in 0.000 seconds

# cProfile.run('composite_3(200)')
# 202 function calls (4 primitive calls) in 0.001 seconds

# cProfile.run('composite_3(500)')
# 502 function calls (4 primitive calls) in 0.002 seconds

# "les_4_task_1.composite_3(100)"
# 1000 loops, best of 5: 130 usec per loop

# "les_4_task_1.composite_3(200)"
# 1000 loops, best of 5: 264 usec per loop

# "les_4_task_1.composite_3(500)"
# 1000 loops, best of 5: 675 usec per loop
