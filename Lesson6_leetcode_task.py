from random import randint
"""Еле осилил. Куча повторяющихся циклов, но других идей так и не появилось
Accepted
Runtime:    41 ms
Your input  [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output      [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Expected    [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
"""


# Проход по столбцам, вперед и в обратном направлении
def add_to_result(i):
    for j in range(1, len(matrix[i]) - 1):
        if matrix[i][j] == 'O' and ((i, j - 1) in result or (i - 1, j) in result):
            result.append((i, j))
    for j in range(len(matrix[i]) - 2, 0, -1):
        if matrix[i][j] == 'O' and ((i, j + 1) in result or (i + 1, j) in result):
            result.append((i, j))


# Проход по строкам
def finding_wrapper_o():
    for i in range(1, len(matrix) - 1):
        add_to_result(i)
    for i in range(len(matrix) - 2, 0, -1):
        add_to_result(i)


# Создание случайной матрицы заданного размера
symbol = {1: 'X', 2: 'O'}
n = int(input('Введите размер поля: '))
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(symbol[randint(1, 2)])
    matrix.append(row)
# matrix = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]

# Вывод базовой матрицы
for item in matrix:
    print('  '.join(item))
result = []
# Добавляем в список на "не замену" элементы "О", стоящие на границе матрицы
for i in range(len(matrix)):
    if i == 0 or i == len(matrix) - 1:
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'O':
                result.append((i, j))
    else:
        for j in [0, len(matrix[i]) - 1]:
            if matrix[i][j] == 'O':
                result.append((i, j))

# Отталкиваясь от граничных элементов, ищем в матрицы "О" и, если они граничат с элементами из списка "не удаления" -
# тоже добавляем их индексы в этот список
finding_wrapper_o()
# z - Счетчик замененных элементов. Изночально был нужен для отладки, решил оставить
z = 0
# Собственно, заменяем все элементы, равные "О" и не находящиеся в списке "не удаления", на "Х"
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'O' and (i, j) not in result:
            matrix[i][j] = 'X'
            z += 1
# вывод результата
print('-'*50)
for item in matrix:
    print('  '.join(item))
print('-'*50)
print(f'Количество замененных символов: {z}')
