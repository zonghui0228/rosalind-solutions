# Enumerating Oriented Gene Orderings

# A signed permutation of length n is an ordering of the first n positive integers 
# in which each integer is then provided with either a positive or negative sign.
def SignedPermutation(n):
	import itertools
	list1 = []
	for i in range(n):
		list1.append(i + 1)
		list1.append(- i - 1)
	# print list1
	list2 = list(itertools.permutations(list1, n))
	# print list2
	list3 = []
	for a in list2:
		aset = set()
		for i in a:
			aset.add(abs(i))
		if len(aset) < len(a):
			list3.append(a)
	# print list3
	# print list4
	list4 = list(set(list2) ^ set(list3))
	print len(list4)
	for i in list4:
		a = str(i)
		# print a
		a = a.replace('(', '')
		a = a.replace(',', '')
		a = a.replace(')', '')
		print a
		
# SignedPermutation(3)
