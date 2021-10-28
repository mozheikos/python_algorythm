"""При вызове функции для нахождения 1000го элементаанализ производительности
показал ускорение во времени выполнения алгоритма при
использованиии решета Эратосфена в 60 раз"""

import cProfile

simple_number = int(input('Введите номер простого числа: '))


def not_eratosphen(n):
    count = 0
    number = 2
    result = 0
    while count != n:
        _ = 0
        for i in range(2, number):
            if number % i == 0:
                _ += 1
        if not _:
            count += 1
            result = number
        number += 1
    return result


def eratosphen(n):
    length = n * 10
    base_list = set(range(2, length + 1))
    result = []
    while base_list:
        number = min(base_list)
        result.append(number)
        base_list -= set(range(number, length + 1, number))
    return result[n - 1]


def main():
    print(f'{simple_number}-е по счету простое число - {not_eratosphen(simple_number)}')
    print(f'{simple_number}-е по счету простое число - {eratosphen(simple_number)}')


cProfile.run('main()')
