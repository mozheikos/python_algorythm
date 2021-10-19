valid_signs = ('0', '+', '-', '*', '/') # Допустимые значения знака
while True:
    num_1 = float(input('Введите операнд №1: '))
    num_2 = float(input('Введите операнд №2: '))
    sign = input('Введите действие (+, -, *, /) или 0 для выхода: ')
    while sign not in valid_signs: # Проверка введенного знака
        sign = input('Вы ввели не правильный знак, попробуйте снова: ')
    if sign == '0': # Вычисления
        break
    elif sign == '+':
        print(f'{num_1} + {num_2} = {num_1 + num_2}')
    elif sign == '-':
        print(f'{num_1} - {num_2} = {num_1 - num_2}')
    elif sign == '*':
        print(f'{num_1} x {num_2} = {num_1 * num_2}')
    elif sign == '/':
        if num_2 == 0:
            print('Ошибка. Деление на ноль')
        else:
            print(f'{num_1} / {num_2} = {num_1 / num_2}')
