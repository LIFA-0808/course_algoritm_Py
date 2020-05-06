# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


alphabet = 'abcdefghijklmnopqrstuvwxyz'
request = int(input('Введите номер буквы в алфавите a-z: '))
if 1 <= request <= 26:
    answer = alphabet[request - 1]
    print(answer)
else:
    print('Неверный ввод')
