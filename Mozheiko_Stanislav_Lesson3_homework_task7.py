from random import randint

# Генерируем случайный список
n = int(input('Введите количество элементов списка: '))
m = int(input('Введите максимальный разряд для элементов списка: '))
base_list = [randint(-1 * 10 ** m + 1, 10 ** m - 1) for i in range(n)]
# Выводим его на экран
print(f'Исходный список - {base_list}')
base_list.sort()    # сортируем по возрастанию и берем первые два элемента
print(f'Минимальные элементы: {base_list[0]}, {base_list[1]}')
