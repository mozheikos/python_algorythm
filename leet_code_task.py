from itertools import zip_longest
l1 = [9, 9, 0, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
# Думаю, самый простой вариант решения этой задачи - сложить 2 числа "столбиком"
in_mind = 0 # переменная "в уме", для единицы
result = []
for item in zip_longest(l1, l2, fillvalue=0):
    _res = sum(item) + in_mind
    result.append(_res % 10)
    in_mind = _res // 10
if in_mind:
    result.append(in_mind)  # Если после сложения последнего разряда в уме осталась единица - ее тоже нужно
    # добавить в список
print(result)
"""на решение ушло минут 20"""
