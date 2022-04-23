array = [3, 6, 2, 1, 7, 8, 5, 9, -1, 10, -45]
print(array)

def sorting(array):
    increament = int(len(array) // 2)
    while increament >= 1:
        for i in range(len(array) - increament):
            for j in range(i + increament, len(array), increament):
                if array[j] < array[i]:
                    array[j], array[i] = array[i], array[j]
        increament -= 2

sorting(array)
print('-'*20, array, sep='\n')
