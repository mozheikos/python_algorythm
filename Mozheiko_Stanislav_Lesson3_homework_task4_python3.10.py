from random import randint

# Генерируем случайный список
n = int(input('Введите количество чисел в списке: '))
m = int(input('Введите максимальный разряд чисел: '))
base_list = [randint(1, 10 ** m - 1) for i in range(n)]
count = 0
for i in set(base_list):
    count_i = base_list.count(i)
    match count_i:
        case count_i if count_i > count:
            element = [i]
            count = count_i
        case count_i if count_i == count:
            element.append(i)
            count = count_i
        case _:
            pass
if count == 1:
    element = 'Все элементы уникальны'
else:
    element = ', '.join(list(map(str, element)))
print(f'В массиве: {base_list}\nЧаще всего встречается элемент: {element}\nКоличество вхождений: {count}')