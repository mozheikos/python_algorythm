from random import randint

n = int(input('Введите количество чисел в списке: '))
m = int(input('Введите максимальный разряд чисел: '))
base_list = [randint(-1 * 10 ** m + 1, 10 ** m - 1) for i in range(n)]
# Создаем список, включаем в него только отрицательные элементы из базового списка
result_list = [i for i in base_list if i < 0]
# Находим максимальный элемент во вспомогательном списке
result = result_list[0]
for item in result_list:
    if item > result:
        result = item
# В основном списке находим индексы элементов, равных найденному
result_index = []
for i in range(len(base_list)):
    if base_list[i] == result:
        result_index.append(i)
print(f'Список: {base_list}\nмаксимальный отрицательный элемент: {result}\nКоличество таких элементов: ' 
    f'{len(result_index)}\nИндексы: {", ".join(list(map(str, result_index)))}')
