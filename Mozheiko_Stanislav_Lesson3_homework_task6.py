from random import randint


def max_min(array):  # Нахождение максимума и минимума.
    result = sorted(array)
    return result[0], result[-1]


# Генерируем случайный список
n = int(input('Введите количество элементов списка: '))
m = int(input('Введите максимальный разряд для элементов списка: '))
base_list = [randint(-1 * 10 ** m + 1, 10 ** m - 1) for i in range(n)]
# Находим максимум и минимум списка
min_item, max_item = max_min(base_list)
# определяем индексы первого вхождения максимума и минимума
index_max = base_list.index(max_item)
index_min = base_list.index(min_item)
# Для корректного подсчета суммы элементов необходимо взять срез от меньшего к большему индексу,
# вне зависимости от того, какой из них - индекс максимума, а какой - минимума
if index_min > index_max:
    index_min, index_max = index_max, index_min
result = sum(base_list[index_min + 1:index_max])    # считаем сумму
# Выводим результат
print(f'Исходный список: {base_list}\nМаксимум: {max_item}, Минимум: {min_item}\nСумма = {result}')
