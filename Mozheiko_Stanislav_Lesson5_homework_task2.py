"""Долго думал как же добавить правильное количество нулей с правильной стороны в слагаемые
при умножении - пришлось у Вас подсмотреть"""
from itertools import zip_longest
# На основании Вашей ремарки на лекции (так вышло, что не успел сдать задание в 3 дня, работа...),
# заменил 16 на константу
BASE = 16


# Суммирование. Я понимаю, что этот алгоритм напоминает Ваше решение, но я честно до него дошел сам,
# еще когда делал задание на литкоде для прошлого урока (Вы видели его)
# в функции суммирования использую *args, так как она будет использована и для умножения,
# а там количество суммируемых числе будет зависеть от количества разрядов умножаемых чисел
def hex_sum(*args):
    in_mind = 0
    add_result_dec = []
    for item in zip_longest(*args, fillvalue=0):
        digit = sum(item) + in_mind
        add_result_dec.append(digit % BASE)
        in_mind = digit // BASE
    if in_mind:
        add_result_dec.append(in_mind)
    return translator(add_result_dec, flag=16)


# Умножение.
def hex_mult(num_1, num_2):
    result = []
    for i in range(len(num_1)):
        _result = []
        if i:
            _result += ['0'] * i
            _result = list(map(int, _result))
        in_mind = 0
        for j in num_2:
            digit = num_1[i] * j + in_mind
            in_mind = digit // BASE
            _result.append(digit % BASE)
        if in_mind:
            _result.append(in_mind)
        result.append(_result)
    return hex_sum(*result)


# Функция обеспечивающая перевод из одной системы счисления в другую. По флагу 10 - в десятичную,
# по флагу 16 - в 16-ричную, возвращая результат в виде развернутого
# списка символов, "годного к дальнейшему употреблению"
def translator(number, flag):
    # Создаем словарь для конвертации числовых форматов. Цифры взял по чару, чтобы сразу получить строковое,
    # хотя можно было [str(i) for i in range(10)]
    hex_digits = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 71)]
    translate_dict = dict(zip(range(BASE), hex_digits))
    result_list = []
    if flag == 10:
        for i in range(len(number)):
            for integer, hexagonal in translate_dict.items():
                if hexagonal == number[i]:
                    result_list.append(integer)
        return result_list[::-1]
    elif flag == 16:
        for i in range(len(number)):
            for integer in translate_dict.keys():
                if integer == number[i]:
                    result_list.append(translate_dict[integer])
        return result_list[::-1]


# Вводим числа с клавиатуры
number_1 = list(input('Введите первое число в 16-ричном формате: '))
number_2 = list(input('Введите второе число в 16-ричном формате: '))
dec_number_1 = translator(number_1, flag=10)
dec_number_2 = translator(number_2, flag=10)
print(f'Сумма чисел {number_1} и {number_2} = {hex_sum(dec_number_1, dec_number_2)}')
print(f'Произведение чисел {number_1} и {number_2} = {hex_mult(dec_number_1, dec_number_2)}')
