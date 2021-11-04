import random


def solution(some_list):
    i = 1
    while True:
        if i not in some_list:
            return i
        i += 1


a = int(input('Введите минимальное значение: '))
b = int(input('Введите максимальное значение: '))
n = int(input('Введите длину списка: '))
init_list = [random.randint(a, b) for i in range(n)]
print(f'Список: {init_list}')
print(f'Минимальное положительное число, не вошедшее в список: {solution(init_list)}')

"""Accepted
Runtime: 50 ms
Your input  [1,2,0]
Output      3
Expected    3"""
