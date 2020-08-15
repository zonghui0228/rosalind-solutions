# ^_^ coding:utf-8 ^_^

"""
Independent Segregation of Chromosomes
url: http://rosalind.info/problems/indc/

Given: A positive integer n≤50.
Return: An array A of length 2n in which A[k] represents the common logarithm of the probability that two diploid siblings share at least k of their 2n chromosomes (we do not consider recombination for now).
"""

import numpy as np

with open("../data/rosalind_indc.txt", "r") as f:
    n = int(f.readline().strip())

p = 0.5
# n = 5
Pr = 0
A = []
for k in range(2*n, 0, -1):
    Pr += np.math.factorial(2*n)/(np.math.factorial(k)*np.math.factorial(2*n-k)) * np.power(p,k)*np.power(1-p, 2*n-k)
    A.append(round(np.log10(Pr), 3))
for i in A[::-1]:
    print(i, end=" ")
