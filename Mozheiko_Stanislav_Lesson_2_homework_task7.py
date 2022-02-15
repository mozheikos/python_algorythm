n = int(input('Введите N: '))
summ = 0
for i in range(n):
    summ += i + 1
summ_1 = n * (n + 1) / 2
if summ == summ_1:
    print(f'1 + 2 +....+ n = {float(summ)}')
    print(f'n(n + 1)/2 = {summ_1}')
    print(f'Равенство 1 + 2 +....+ n = n(n + 1)/2 верно')
