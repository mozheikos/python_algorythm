from random import randint

# Создаем случайную матрицу 4х4
matrix = []
for row in range(4):
    row = [randint(1, 10) for i in range(4)]
    row.append(sum(row))    # считаем сумму элементов строки, добавляем в конец той же строки
    matrix.append(row)  # добавляем строку в матрицу
for item in matrix:     # Вывод полученной матрицы
    print(f'{item}')
