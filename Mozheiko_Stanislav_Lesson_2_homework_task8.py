import random
n = int(input('Введите количество чисел в последовательности: '))
q = int(input('Введите максимальный разряд чисел: '))   # решил немного добавить вариативности
numbers = []
for i in range(n):
    numbers.append(random.randint(1, 10**q-1))  # генерируем ряд чисел
digit = int(input('Введите искомую цифру: '))
count = 0
for number in numbers:  # В каждом числе перебираем цифры, сравнивая с искомой. При совпадении увеличиваем счетчик
    while number != 0:
        finding = number % 10
        if finding == digit:
            count += 1
        number //= 10
print(f'Ваша последовательность: {" ".join(list(map(str, numbers)))}')
print(f'Цифра {digit} встречается в введенной последовательности {count} раз')
