"""Год является високосным в 2 случаях:
1) номер оканчивается двумя нулями и делится на 400
2) номер не оканчивается двумя нулями и делится на 4
* Берем года только нашей эры"""
year = input('Введите год: ')
# Валидация
if not year.isdigit():
    print('Не верно введенный номер года')
    exit(0)
else:
    year = int(year)
    answer = 'Нет'
    if year % 4 == 0:
        answer = 'Да'
    elif year % 100 == 0 and year % 400 == 0:
        answer = 'Да'
    print(f'Високосный ли {year} год: - {answer}')
