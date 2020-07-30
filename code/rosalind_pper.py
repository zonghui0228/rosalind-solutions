# ^_^ coding:utf-8 ^_^

"""
Partial Permutations
url: http://rosalind.info/problems/pper/

Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.
Return: The total number of partial permutations P(n,k), modulo 1,000,000.
"""

def fac(n):
	f = 1
	for i in range(n):
		f *= (i+1)
	return f

def p_per(n, k):
	return fac(n)/fac(n-k) % 1000000

print(p_per(96, 9))