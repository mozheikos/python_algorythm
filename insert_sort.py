array = [3, 6, 2, 1, 7, 8, 5]

def sorting(array):
    a = [array[0]]
    for i in range(1, len(array)):
        j = 0
        while j < len(a):
            if array[i] < a[j]:
                a.insert(j, array[i])
                break
            j += 1
        else:
            a.append(array[i])
        print(a)
    return a

sorted_array = sorting(array)
print('-'*20, array, sorted_array, sep='\n')
