from collections import namedtuple

factory_count = int(input('Введите количество предприятий: '))
factory_info = dict.fromkeys(range(factory_count))
for key in factory_info.keys():
    title = input(f'Введите название предприятия {key + 1}: ')
    Income = namedtuple('Income', 'first second third fourth')
    quoters = list(map(float, input('Введите прибыли перлприятия зв 1 2 3 4 квартал через пробел: ').split(' ')))
    income = Income(*quoters)
    factory_info[key] = {'title': title, 'income': income}
total_avg_income = 0
for factory in factory_info.values():
    total_avg_income += sum(factory['income'])
total_avg_income = total_avg_income / factory_count
above_avg = []
below_avg = []
for factory in factory_info.values():
    factory['total_income'] = sum(factory['income'])
    if factory['total_income'] > total_avg_income:
        above_avg.append(factory)
    elif factory['total_income'] < total_avg_income:
        below_avg.append(factory)
print(f'Средняя прибыль за год для всех предприятий: {total_avg_income:0.2f}')
print(f'Годовая прибыль выше среднего у {len(above_avg)} предприятий:')
for item in above_avg:
    print(f'{item["title"]}: {item["total_income"]} руб')
print(f'Годовая прибыль ниже среднего у {len(below_avg)} предприятий:')
for item in below_avg:
    print(f'{item["title"]}: {item["total_income"]} руб')
