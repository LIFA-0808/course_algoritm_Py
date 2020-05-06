# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.


alphabet = 'abcdefghijklmnopqrstuvwxyz'
borders = sorted(input('Введите 2 буквы a-z: ').lower().split('-'))
answer = len(alphabet[alphabet.index(borders[0]):alphabet.index(borders[1])+1]) - 2
print(answer)
