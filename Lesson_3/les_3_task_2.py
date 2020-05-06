# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
from random import randint

size = randint(1, 100)
array_1 = list(set([randint(1, 100) for i in range(size)]))
array_2 = []
for i in array_1:
    if i % 2 == 0:
        array_2.append(array_1.index(i))
print(f'array_1 = {array_1}')
print(f'array_2 = {array_2}')
