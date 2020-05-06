# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
from random import randint

size = randint(1, 20)                             # определяем случайный массив
array = [randint(-10, 10) for i in range(size)]
print(f'array = {array}')

max_negative = -10                                # находим макссимальный отрицательный элемент
for i in array:
    if 0 > i > max_negative:
        max_negative = i

if max_negative > 0:                              # выводим результат
    print('В массиве нет отрицательных значений')
else:
    index_num = [i for i, x in enumerate(array) if x == max_negative]
    print(f'Максимальный отрицательный элемент "{max_negative}": на позиции(-ях){index_num} ')
