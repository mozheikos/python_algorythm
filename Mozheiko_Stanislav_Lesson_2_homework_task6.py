import random

number = random.randint(0, 100)
count = 1
print('Компьютер загадал случайное число. Попробуйте его отгадать.')
while count <= 10:
    user = int(input(f'Попытка №{count}. Ваш ответ: '))
    if user == number:
        print(f'Отлично. Вы угадали! Правильный ответ: {number}. Попыток использовано: {count}')
        break
    else:
        if user < number:
            print(f'Вы ввели {user}. Загаданное число больше. Попробуйте еще')
        else:
            print(f'Вы ввели {user}. Загаданное число меньше. Попробуйте еще')
        count += 1
else:
    print(f'К сожалению, Вы проиграли. Попыток больше нет. Правильный ответ - {number}')
