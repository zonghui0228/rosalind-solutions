#coding:utf-8
def num_rabbits(n, m):
	# n is the n-th month.
	# m is that a rabbit live for m month.
	# in the first month, the num of rabbit is 1. 
	num_list = []
	num_list.append(0)
	num_list.append(1)
	for i in range(1, n+1, 1):

		if i < m:
			num_list.append(num_list[i] + num_list[i-1])
			print i
			print num_list
		if i == m:
			num_list.append(num_list[i] + num_list[i-1] - num_list[i-m+1])
			print i
			print num_list
		if i > m:
			num_list.append(num_list[i] + num_list[i-1] - num_list[i-m])
			print i
			print num_list
#计算第i个月该死亡的兔子，也即i-m个月的幼年兔子数量=i-m-1个月之前的成年兔子总数
	print num_list
	print num_list[n]
num_rabbits(6, 3)