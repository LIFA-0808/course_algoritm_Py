# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


result = 0
max_num = 0
m = int(input('Введите колличество чисел: '))
for j in range(m):
    num = int(input('Введите число: '))
    if num > max_num:
        result = 0
        max_num = num
        example = str(num)
        for d in example:
            result += int(d)
print(f'Наибольшее число - {max_num}: сумма цифр = {result}')
