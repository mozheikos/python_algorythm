from memory_profiler import profile

simple_number = int(input('Введите номер простого числа: '))


@profile
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


@profile
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


if __name__ == '__main__':
    main()

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    23     19.1 MiB     19.1 MiB           1   @profile
    24                                         def eratosphen(n):
    25     19.1 MiB      0.0 MiB           1       length = n * 10
    26     19.1 MiB      0.0 MiB           1       base_list = set(range(2, length + 1))
    27     19.1 MiB      0.0 MiB           1       result = []
    28     19.1 MiB      0.0 MiB          26       while base_list:
    29     19.1 MiB      0.0 MiB          25           number = min(base_list)
    30     19.1 MiB      0.0 MiB          25           result.append(number)
    31     19.1 MiB      0.0 MiB          25           base_list -= set(range(number, length + 1, number))
    32     19.1 MiB      0.0 MiB           1       return result[n - 1]


10-е по счету простое число - 29

Видим использование памяти в 19.1 МБ
"""