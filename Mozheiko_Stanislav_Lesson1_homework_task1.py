number = input('Введите трехзначное число: ')
print(f'Ваше число: {number}')
# исключаем ошибку при введении отрицательного числа (оно ведь все равно трехзначное)
if number[0] == '-':
    number = number[1:]
# берем только данные состоящие из трех цифра, любые другие варианты уйдут в ELSE
if number.isdigit() and len(number) == 3:
    n1, n2, n3 = map(int, list(number))
    answer = f'Сумма = {n1 + n2 + n3}\nПроизведение = {n1 * n2 * n3}'
else:
    answer = f'Вы ввели неверные данные {number}'
print(answer)
