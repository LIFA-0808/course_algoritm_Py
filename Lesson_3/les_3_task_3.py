# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

size = randint(1, 10)                             # определяем случайный массив
array = [randint(1, 100) for i in range(size)]
print(f'array = {array}')

max_num = 0                                       # определяем минимум и максимум
min_num = array[0]
for item in array:
    if item > max_num:
        max_num = item
    if item < min_num:
        min_num = item
print(f'max_num = {max_num}')
print(f'min_num = {min_num}')

pos_max = array.index(max_num)                     # меняем местами минимум и максимум
pos_min = array.index(min_num)
max_num, min_num = min_num, max_num
array[pos_max] = max_num
array[pos_min] = min_num
print(f'new_array = {array}')
