# coding:utf-8
# Enumerating Gene Orders
# 排列

# Sample Dataset
# 3
# Sample Output
# 6
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

def Permutation(n):
	import itertools
	list1 = []
	for i in range(n):
		list1.append(i + 1)
	# print list1
	list2 = list(itertools.permutations(list1, n))
	print len(list2)
	for i in list2:
		i = str(i).replace('(', '')
		i = i.replace(')', '')
		i = i.replace(',', '')
		print i
# Permutation(6)