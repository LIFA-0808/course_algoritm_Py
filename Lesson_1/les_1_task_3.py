# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
from random import randint, uniform, choice


operation = input('''Введите тип операции: 
a - случайное целое число,
b - случайное вещественное число,
c - случайный символ (a-z)
exit - для выхода
_''')

if operation == 'a' or operation == 'b' or operation == 'c':
    borders = input('Введите границы диапазона - i-j: ')
    if operation == 'a':
        borders = sorted(list(map(int, borders.split('-'))))
        answer = randint(borders[0], borders[1])
    elif operation == 'b':
        borders = sorted(list(map(float, borders.split('-'))))
        answer = uniform(borders[0], borders[1])
    else:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        borders = sorted(borders.lower().split('-'))
        sequence = alphabet[alphabet.index(borders[0]):alphabet.index(borders[1])+1]
        answer = choice(sequence)
    print(answer)
else:
    print('Завершение программы')
