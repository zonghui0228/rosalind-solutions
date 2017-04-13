# coding: utf-8
# 插入排序
# 每次找最小值
# 最坏的情况下复杂度为list长度的平方
def ins(array):
	swap = 0
	for i in range(len(array)):
		k = i
		while k > 0 and array[k] < array[k-1]:
			array[k-1], array[k] = array[k], array[k-1]
			swap += 1
			k -= 1
	# return array 返回排序后的列表
	return swap        # 返回交换次数


# f = open('rosalind_ins.txt', 'r')
# f.readline()
# s = [int(i) for i in f. readline().strip().split(' ')]
# print ins(s)