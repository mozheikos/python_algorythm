from itertools import zip_longest
from memory_profiler import profile
"""Задача из литкод для урока 3"""


@profile(precision=4)
def main():
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    in_mind = 0
    result = []
    for item in zip_longest(l1, l2, fillvalue=0):
        _res = sum(item) + in_mind
        result.append(_res % 10)
        in_mind = _res // 10
    if in_mind:
        result.append(in_mind)
    print(result)


if __name__ == '__main__':
    main()
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5  19.1250 MiB  19.1250 MiB           1   @profile(precision=4)
     6                                         def main():
     7  19.1250 MiB   0.0000 MiB           1       l1 = [2, 4, 3]
     8  19.1250 MiB   0.0000 MiB           1       l2 = [5, 6, 4]
     9  19.1250 MiB   0.0000 MiB           1       in_mind = 0
    10  19.1250 MiB   0.0000 MiB           1       result = []
    11  19.1367 MiB   0.0078 MiB           4       for item in zip_longest(l1, l2, fillvalue=0):
    12  19.1367 MiB   0.0000 MiB           3           _res = sum(item) + in_mind
    13  19.1367 MiB   0.0039 MiB           3           result.append(_res % 10)
    14  19.1367 MiB   0.0000 MiB           3           in_mind = _res // 10
    15  19.1367 MiB   0.0000 MiB           1       if in_mind:
    16                                                 result.append(in_mind)
    17  19.1367 MiB   0.0000 MiB           1       print(result)

В данном примере видим использование памяти: сначала 19.125Мб на создание списков и функций,
далее увеличение на функцию zip_longest и на добавление элементов в список result (расширение списка)
"""
