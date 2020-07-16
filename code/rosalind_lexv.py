# string = 'DNA'
# n = 3
# for i1 in range(len(string)):
# 	print string[i1],
# 	for i2 in range(len(string)):
# 		print string[i1] + string[i2],
# 		for i3 in range(len(string)):
# 			print string[i1] + string[i2] + string[i3],

# D DD DDD DDN DDA DN DND DNN DNA DA DAD DAN DAA N ND NDD NDN NDA NN NND NNN NNA NA NAD NAN NAA
# A AD ADD ADN ADA AN AND ANN ANA AA AAD AAN AAA


def lexv(alphabet, n):
	import itertools
	result = []
	for i in range(n):
		for j in list(itertools.product(alphabet, repeat = i + 1)):
			result.append("".join(j))
	return result
	# not sort 
# alphabet = 'DNA'
# n = 3
# print lexv(alphabet, n)