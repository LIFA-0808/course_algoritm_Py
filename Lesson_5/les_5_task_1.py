# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для
# каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import OrderedDict


# Инициализация ввода данных о предприятиях
num = int(input('Введите колличество предприятий: '))
factories = dict()
for factory in range(num):
    name = input('Введите название предприятия: ')
    data = sum([int(input(f'Введите данные о прибыли за {q + 1} квартал: ')) for q in range(4)])
    factories[name] = data

# Подсчёт средней прибыли
total_profit = 0
for key in factories:
    total_profit += factories[key]
average_profit = total_profit/num
print(f'Средняя прибыль предприятий составила {average_profit}')

# Сортировка предприятий по прибыле
profit_list = OrderedDict(sorted(factories.items(), key= lambda x: x[1]))
for k, v in profit_list.items():
    if v > average_profit:
        print(f'Предприятие заработало {k} заработало {v}, что больше средней прибыли {average_profit}')
    elif v < average_profit:
        print(f'Предприятие заработало {k} заработало {v}, что меньше средней прибыли {average_profit}')
