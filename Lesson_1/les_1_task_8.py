# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).


print("Введите три числа:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a != b != c:
    if a > b > c or a < b < c:
        print(f'{b} - среднее число')
    if a > c > b or a < c < b:
        print(f'{c} - среднее число')
    else:
        print(f'{a} - среднее число')
else:
    print('Неверный ввод')
