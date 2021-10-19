number = int(input('Введите любое натуральное число: '))
print(f'Ваше число - {number}')
chet = 0
nechet = 0
while number != 0:
    if (number % 10) % 2 == 0:     # четные
        chet += 1
    else:   # нечетные
        nechet += 1
    number //= 10
print(f'Четных - {chet}, Нечетных - {nechet}')
