# coding: utf-8
def building_a_heap(array):
	# for j in range(len(array)):
	for i in range(len(array), 1, -1):
		# print array[i-1]
		if array[i/2-1] < array[i-1]:
			# print i, array[i/2-1], array[i-1]
			array[i/2-1], array[i-1] = array[i-1], array[i/2-1]
		# print array
	return array  




if __name__ == '__main__':
	a = [1, 3, 5, 7, 2]
	print building_a_heap(a)
# print / 2