import hashlib
"""Может я недопонял, но вроде так. Функция делает обход строки, перебирая все возможные подстроки. Так как сравниваем 
строку с самой собой - при достаточно короткой строке без повторов символов на каждой итерации будет только одно 
совпадение. Соответственно, обход по средствам функции (точнее - итератора), ну и сравниваем, переводя в хэш"""


def walk(string):
    len_substring = 1  # Длинна подстроки. изменяется от 1 (символ) до строка - 1 (полную строку сказано не сравнивать
    while len_substring < len(s):
        # Начало итерации. Нужно чтобы реально проверить все. Ведь в
        # слове АРАРАТ, например, подстрока АР встретится дважды: с началом 0 и длинной 2 и с началом 2 длинной 2,
        # а суммарно совпадений будет много для такого короткого слова, так как букв всего 3.
        for start in range(len(s) - len_substring + 1):
            length = len_substring + start
            yield string[start:length]
        len_substring += 1


# s = 'АРАРАТ'
s = 'string'
count = 0
for i in walk(s):
    for j in walk(s):
        if hashlib.sha256(i.encode()).hexdigest() == hashlib.sha256(j.encode()).hexdigest():
            count += 1
print(f'Строка {s} содержит в себе подстрок: {count}')
