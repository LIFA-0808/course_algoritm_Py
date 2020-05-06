# 4. Определить, какое число в массиве встречается чаще всего.
from random import randint

size = randint(1, 100)                             # определяем случайный массив
array = [randint(1, 10) for i in range(size)]
often_num = 0
print(f'array = {array}')


results = [0 for _ in range(11)]                   # находим сколько раз повторяются элементы
for i in array:
    for num in range(11):
        if i == num:
            results[num] += 1
print(results)

for i in results:                                 # определяем самый частый(-ые) элемент(ы) и выводим
    if i > often_num:
        often_num = i
index_num = [i for i, x in enumerate(results) if x == often_num]
print(f'Чаще всего в массиве встречается {index_num}: {often_num} раз(-а)')
