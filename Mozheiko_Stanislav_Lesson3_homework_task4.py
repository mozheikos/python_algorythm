from random import randint

# Генерируем случайный список
n = int(input('Введите количество чисел в списке: '))
m = int(input('Введите максимальный разряд чисел: '))
base_list = [randint(1, 10 ** m - 1) for i in range(n)]
count = 0
element = []    # Элементы в виде списка, для того, чтобы вывести все, если условию задачи удовлетворяет несколько
# элементов
for i in set(base_list):    # Перебираем элементы множества для уменьшения количества проходов и отсутствия дублирования
    count_i = base_list.count(i)
    if count_i >= count:
        if count_i > count:     # В случае, если нашелся элемент, встречающийся чаще, чем предыдущий промежуточный
            # результат - список нужно очистить
            element.clear()
        element += [i]
        count = count_i
if count == 1:
    element = 'Все элементы уникальны'
else:
    element = ', '.join(list(map(str, element)))
print(f'В массиве: {base_list}\nЧаще всего встречается элемент: {element}\nКоличество вхождений: {count}')
