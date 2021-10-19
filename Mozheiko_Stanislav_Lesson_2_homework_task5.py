order = list(range(32, 128))
row = 10
i = 0
while i < len(order):
    for row_ in order[i:i + row]:
        print(f'| {str(row_).center(3)} : {chr(row_)} ', end='')
    print()
    i += row
# позиции 32 и 127 - пустые, так как 32й символ - это пробел, а 127й - пустой
