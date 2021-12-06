array = [3, 6, 2, 1, 7, 8, 5]

def sorting(array):
	array_to_sort = array[:]
	i_min = 0
	for i in range(len(array_to_sort)):
	    for j in range(i, len(array_to_sort)):
	        if array_to_sort[j] < array_to_sort[i_min]:
	            i_min = j
	    array_to_sort[i], array_to_sort[i_min] = array_to_sort[i_min], array_to_sort[i]
	return array_to_sort

sorted_array = sorting(array)
print(array, sorted_array, sep='\n')
