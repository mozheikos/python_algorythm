array = [3, 6, 2, 1, 7, 8, 5]
print(array)

def sorting(array):
	i_min = 0
	for i in range(len(array)):
	    for j in range(i, len(array)):
	        if array[j] < array[i_min]:
	            i_min = j
	    array[i], array[i_min] = array[i_min], array[i]
	return array

sorted_array = sorting(array)
print(sorted_array, sep='\n')
