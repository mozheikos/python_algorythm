from random import randint

# Генерируем случайный список
n = int(input('Введите количество элементов списка: '))
base_list = [randint(1, 9) for i in range(n)]
print(base_list)
result = sorted(base_list)  # Сортируем по возрастанию
for i in range(len(base_list)):     # Пробегаем по списку, попутно меняя max на min и наоборот
    if base_list[i] == result[0]:
        base_list[i] = result[-1]
    elif base_list[i] == result[-1]:
        base_list[i] = result[0]
print(base_list)
print(f'Наибольший элемент = {result[-1]}\nНаименьший элемент = {result[0]}')
