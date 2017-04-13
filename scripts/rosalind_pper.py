# Partial Permutations
# an ordering of some of objects from a collection
# A(n, k)  k <= n

# The total number of partial permutations(n,k) , modulo 1,000,000.

# factorial of n
def fac(n):
	f = 1
	for i in range(n):
		f = f * (i+1)
	return f
def p_per(n, k):
	return fac(n)/fac(n-k)

# print p_per(85, 10)