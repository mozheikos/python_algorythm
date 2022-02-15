from random import randint
from memory_profiler import profile
"""Решил использовать задачу из литкода, так как она объемнее. Алгоритмы из дз 1-3 ну совсем короткие"""


def add_to_result(i):
    for j in range(1, len(matrix[i]) - 1):
        if matrix[i][j] == 'O' and ((i, j - 1) in result or (i - 1, j) in result):
            result.append((i, j))
    for j in range(len(matrix[i]) - 2, 0, -1):
        if matrix[i][j] == 'O' and ((i, j + 1) in result or (i + 1, j) in result):
            result.append((i, j))


def finding_wrapper_o():
    for i in range(1, len(matrix) - 1):
        add_to_result(i)
    for i in range(len(matrix) - 2, 0, -1):
        add_to_result(i)


symbol = {1: 'X', 2: 'O'}
n = int(input('Введите размер поля: '))
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(symbol[randint(1, 2)])
    matrix.append(row)
# matrix = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]


@profile
def main():
    for item in matrix:
        print('  '.join(item))

    for i in range(len(matrix)):
        if i == 0 or i == len(matrix) - 1:
            for j in range(len(matrix[i])):
                if matrix[i][j] == 'O':
                    result.append((i, j))
        else:
            for j in [0, len(matrix[i]) - 1]:
                if matrix[i][j] == 'O':
                    result.append((i, j))

    finding_wrapper_o()

    z = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'O' and (i, j) not in result:
                matrix[i][j] = 'X'
                z += 1
    print('-'*50)
    for item in matrix:
        print('  '.join(item))
    print('-'*50)
    print(f'Количество замененных символов: {z}')


if __name__ == '__main__':
    result = []
    main()

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    39     19.4 MiB     19.4 MiB           1   @profile
    40                                         def main():
    41     19.4 MiB      0.0 MiB           7       for item in matrix:
    42     19.4 MiB      0.0 MiB           6           print('  '.join(item))
    43                                         
    44     19.4 MiB      0.0 MiB           7       for i in range(len(matrix)):
    45     19.4 MiB      0.0 MiB           6           if i == 0 or i == len(matrix) - 1:
    46     19.4 MiB      0.0 MiB          14               for j in range(len(matrix[i])):
    47     19.4 MiB      0.0 MiB          12                   if matrix[i][j] == 'O':
    48     19.4 MiB      0.0 MiB           6                       result.append((i, j))
    49                                                 else:
    50     19.4 MiB      0.0 MiB          12               for j in [0, len(matrix[i]) - 1]:
    51     19.4 MiB      0.0 MiB           8                   if matrix[i][j] == 'O':
    52     19.4 MiB      0.0 MiB           6                       result.append((i, j))
    53                                         
    54     19.4 MiB      0.0 MiB           1       finding_wrapper_o()
    55                                         
    56     19.4 MiB      0.0 MiB           1       z = 0
    57     19.4 MiB      0.0 MiB           7       for i in range(len(matrix)):
    58     19.4 MiB      0.0 MiB          42           for j in range(len(matrix[i])):
    59     19.4 MiB      0.0 MiB          36               if matrix[i][j] == 'O' and (i, j) not in result:
    60                                                         matrix[i][j] = 'X'
    61                                                         z += 1
    62     19.4 MiB      0.0 MiB           1       print('-'*50)
    63     19.4 MiB      0.0 MiB           7       for item in matrix:
    64     19.4 MiB      0.0 MiB           6           print('  '.join(item))
    65     19.4 MiB      0.0 MiB           1       print('-'*50)
    66     19.4 MiB      0.0 MiB           1       print(f'Количество замененных символов: {z}')

Из вывода профайлера видно, что вся память (19.4 МБ) была занята при создании матрицы. 
Далее все операции идут 'in place'
"""
