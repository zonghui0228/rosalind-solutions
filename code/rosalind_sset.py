# counting subsets.
# input: a positive integer n (n <= 1000).
# output: the total number of subsets of {1, 2, ..., n} modulo 1,000,000.
def subset(n):
	import math
	s = 0
	for i in range(n+1):
		s += math.factorial(n) / (math.factorial(i) * math.factorial(n-i))
	return s % 1000000
if __name__ == '__main__':
	print subset(883)
	# print 8%1000000