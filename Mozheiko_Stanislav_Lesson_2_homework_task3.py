number = int(input('Введите число: '))
print(f'Вы ввели {number}')
new_number = []
while number != 0:
    new_number.append(number % 10)
    number //= 10
# На этом можно было закончить, сделав:
# new_number.append(str(n))
# print(''.join(new_number)), но раз с цифрами работаем в цифрах и на выходе нужен интежер - то еще один цикл:
new = 0
new_number.reverse()
for i in range(len(new_number)):
    new += new_number[i] * 10**i
print(new)
print(type(new))
