#reverse array without using reverse_function
def reverse_array(array):
	length = len(array)
	mid_size = length/2
	for i in range(0,int(mid_size)):
		store_length = length - i -1
		temp = array[store_length]
		array[store_length] = array[i]
		array[i] = temp
	return [array];


list = reverse_array([2,4,6,1])
print(list)



