"""Для задачи использовал алгоритм задания 6 к уроку 3
Так как самая затратная операция - сортировка, то во втором варианте
я заменил сортировку на функции min и max
анализ производительности со списком в 10000 элементов показал разницу во времени в 11%"""


import cProfile
from random import randint


def max_min(array):
    result = sorted(array)
    return result[0], result[-1]


def max_min_1(array):
    result_1 = min(array)
    result_2 = max(array)
    return result_1, result_2


def main_1():
    n = int(input('Введите количество элементов списка: '))
    m = int(input('Введите максимальный разряд для элементов списка: '))
    base_list = [randint(-1 * 10 ** m + 1, 10 ** m - 1) for i in range(n)]
    min_item, max_item = max_min(base_list)
    index_max = base_list.index(max_item)
    index_min = base_list.index(min_item)
    if index_min > index_max:
        index_min, index_max = index_max, index_min
    result = sum(base_list[index_min + 1:index_max])
    print(f'Исходный список: {base_list}\nМаксимум: {max_item}, Минимум: {min_item}\nСумма = {result}')


def main_2():
    n = int(input('Введите количество элементов списка: '))
    m = int(input('Введите максимальный разряд для элементов списка: '))
    base_list = [randint(-1 * 10 ** m + 1, 10 ** m - 1) for i in range(n)]
    min_item, max_item = max_min_1(base_list)
    index_max = base_list.index(max_item)
    index_min = base_list.index(min_item)
    if index_min > index_max:
        index_min, index_max = index_max, index_min
    result = sum(base_list[index_min + 1:index_max])
    print(f'Исходный список: {base_list}\nМаксимум: {max_item}, Минимум: {min_item}\nСумма = {result}')


def main():
    main_1()
    main_2()


cProfile.run('main()')
