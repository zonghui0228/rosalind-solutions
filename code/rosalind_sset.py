# ^_^ coding:utf-8 ^_^

"""
Counting Subsets
url: http://rosalind.info/problems/sset/

Given: A positive integer n (n≤1000).
Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.
"""

import math
from scipy.special import comb, perm

with open("../data/rosalind_sset.txt", "r") as f:
    n = int(f.readline().strip())
print(n)

s = 0
for i in range(1, n+1):
    # s += int(comb(n, i))
    s += int(math.factorial(n) / (math.factorial(i) * math.factorial(n-i)))
print(s)
print(s%1000000)
