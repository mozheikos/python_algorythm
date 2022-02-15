import random

n = int(input('Введите количество чисел для генерации: '))
q = int(input('Введите максимальный разряд чисел: '))
numbers = []
for i in range(n):  # Генерируем ряд чисел
    numbers.append(random.randint(1, 10**q-1))
answer_number = 0
answer_sum = 0
for num in numbers:     # для каждого из чисел ищем сумму цифр и сравниваем ее с имеющейся максимальной
    number = num
    summ = 0
    while num != 0:
        summ += num % 10
        num = num // 10
    if summ > answer_sum:
        answer_number = number
        answer_sum = summ
print(f'Вы ввели числа {" ".join(list(map(str, numbers)))}')
print(f'У числа {answer_number} сумма цифр наибольшая: {answer_sum}')
