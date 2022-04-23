from random import choice

array = [3, 6, 2, 1, 7, 8, 5, 9, -1, 10]

def sorting(array):
    if len(array) <= 1:
        return array
    else:
        a = array[:]
        wrap = choice(a)
        small = []
        equal = []
        bigger = []
        for i in a:
            if i > wrap:
                bigger += [i]
            elif i == wrap:
                equal += [i]
            else:
                small += [i]
        return sorting(small) + equal + sorting(bigger)

sorted_array = sorting(array)
print('-'*20, array, sorted_array, sep='\n')
