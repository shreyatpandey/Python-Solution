
#makes no use of temporary variable most memory_efficient
def reverse_array_no_tempvariable(nums):
	length = len(nums)
	mid_size = (int)(length/2)
	for i in range(0,mid_size):
		nums[i]=nums[i] + nums[length-i-1]
		nums[length-i-1] = nums[i] - nums[length-i-1]
		nums[i] = nums[i]-nums[length-i-1]
	return nums;
def xor_number(x,y):
	x = x^y
	y = x^y
	x = x^y
	return x,y ;
	


list = reverse_array([2,4,6,1])
list1 = reverse_array_no_tempvariable([2,4,6,1])
print(list)
print(list1)
x,y = xor_number(15,10)







