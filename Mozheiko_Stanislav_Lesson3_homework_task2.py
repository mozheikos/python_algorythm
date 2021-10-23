from random import randint

base_list = []  # Генерируем массив №1
for rand in range(10):
    base_list += [randint(1, 100)]
result = [i for i in range(len(base_list)) if base_list[i] % 2 == 0] # Добавлем в массив №2 только четные элементы
# массива 1
print(f'Исходный массив - {base_list}\nРезультирующий массив (индексация с 0) - {result}')
