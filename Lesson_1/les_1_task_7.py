# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.


year = int(input('Введите год: '))
is_leap = False
if year > 0:
    if year % 4 == 0:
        if year % 100 != 0:
            is_leap = True
        elif year % 400 == 0:
            is_leap = True
    if is_leap:
        print(f'{year} год - високосный')
    else:
        print(f'{year} год - не високосный')
else:
    print('Неверный ввод')


