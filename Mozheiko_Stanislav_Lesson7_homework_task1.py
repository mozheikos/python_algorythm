from random import randint


def bubbles_decreasing(some_array):  # Метод "пузырька"
    iter_count = 0
    while True:
        count = 0
        for i in range(len(some_array) - 1):
            if some_array[i] < some_array[i + 1]:
                some_array[i], some_array[i + 1] = some_array[i + 1], some_array[i]
                count += 1
        iter_count += 1
        if not count:
            return iter_count


n = int(input('Введите длинну массива: '))
array = [randint(-100, 99) for i in range(n)]
print(f'Исходный массив:\n{array}')
iterations = bubbles_decreasing(array)
print(f'Массив, отсортированные по убыванию методом "пузырька":\n{array}\n')
print(f'Затрачено итераций: {iterations}')
