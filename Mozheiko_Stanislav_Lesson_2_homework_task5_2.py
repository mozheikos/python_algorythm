start_code = 32  # начало диапазона символов
end_code = 127  # конец диапазона символов
count = 0  # счетчик длинны строки
row = 10  # заданная длинна строки
for i in range(start_code, end_code + 1):
    print(f'| {str(i).center(3)} : {chr(i)} ', end='')
    count += 1
    if count % row == 0:  # После каждого десятого элемента закрываем границу таблицы и делаем перенос строки
        print('|')
