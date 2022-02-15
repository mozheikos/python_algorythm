import random

user_input_start = input(f'Введите начало диапазона\n- чисел - если хотите получить случайное число\n -символов - для '
                    f'генерации случайной буквы\n')
user_input_end = input(f'Введите конец диапазона: ')
# скидываю значения в список, чтобы проще было менять типы данных и для сортировки по возрастанию
user_range = [user_input_start, user_input_end]
# проверяем на буквы
if user_input_start.isalpha() and user_input_end.isalpha():
    user_range = sorted(list(map(ord, user_range)))
    answer = chr(random.randint(user_range[0], user_range[1]))
else: # из оставшегося кроме букв исключаем прочие знаки при помощи try-except
    try:
        user_range = sorted(list(map(float, user_range)))
    except ValueError:
        answer = 'Ошибка при вводе диапазона'
    else: # раздеяем на целые и вещественные методом проверки остатка от деления. В случае дроби хотя бы на одной
        # границе диапазона - диапазон считается дробным
        if user_range[0] % 1 == 0 and user_range[1] % 1 == 0:
            answer = random.randint(int(user_range[0]), int(user_range[1]))
        else:
            answer = round(random.uniform(user_range[0], user_range[1]), 1)
print(answer)
