from random import randint
"""Так и не получилось у меня  О(log n), но, думаю, все равно оптимальнее чем сортировка (О(n/2)) если я правильно 
понимаю"""


def sorting_mediana(some_array):
    num = sorted(some_array)
    print(f'Список после сортировки:\n{num}\n')
    return num[len(num) // 2]


def unsorting_mediana(some_array):
    count = len(some_array) // 2

    def finding(arr):
        n = max(arr)
        temp = [i for i in arr if i < n]
        if len(temp) > count:
            return finding(temp)
        else:
            return n

    return finding(some_array)


m = int(input('Введите половину длины массива: '))
array = [randint(1, 100) for i in range(2 * m + 1)]
print(f'Изначальный список:\n{array}\n')
print(f'Медиана списка, полученная методом сортировки: {sorting_mediana(array)}')
print(f'Медиана списка, полученная методом без сортировки: {unsorting_mediana(array)}')
