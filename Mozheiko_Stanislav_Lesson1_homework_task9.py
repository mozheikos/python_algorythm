# Валидация
try:
    # вносим все 3 числа в список, сортируем по возрастанию и берем второе) и никаких проверок
    numbers = sorted(list(map(float, input('Введите 3 любых числа: ').split())))
except ValueError:
    print('Вы ввели не число')
    exit(0)
else:
    print(f'Вы ввели: {numbers[0]}, {numbers[1]}, {numbers[2]}. Средним является {numbers[1]}')