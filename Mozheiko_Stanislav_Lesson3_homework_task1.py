start = 2   # Начало интервала
end = 99    # Конец интервала
answer = dict.fromkeys(range(2, 10), 0)     # Вместо двумерного массива решил, что удобнее хранить результат в словаре
for i in range(start, end + 1):
    for j in answer.keys():
        if i % j == 0:
            answer[j] += 1
print(f'В диапазоне {start} - {end} ')
for i in answer.keys():
    print(f'На {i} делится {answer[i]} чисел')
