from random import random


# Функция слияния
def merging(list_1, list_2):
    result = []
    i = 0
    j = 0
    # Передвигаясь по отсортированным спискам, сравниваем элементы на одной и той же позиции и меньший добавляем в
    # результирующий список. Увеличиваем тот счетчик, в чьем массиве оказался минимальный элемент
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1
    # Если один из списков был длиннее - после перебора добавляем оставшиеся элементы в конец
    if len(list_1) > i:
        result.extend(list_1[i:])
    elif len(list_2) > j:
        result.extend(list_2[j:])
    return result


# Основная функция
def sorting(some_array):
    if len(some_array) == 1:  # Конец рекурсии
        return some_array
    else:
        half = len(some_array) // 2  # Середина списка
        a = sorting(some_array[:half])
        b = sorting(some_array[half:])
        return merging(a, b)


n = int(input('Введите длинну списка: '))
array = [round((random() * 50 - 0.1), 1) for i in range(n)]
print(array)
array = sorting(array)
print(array)
