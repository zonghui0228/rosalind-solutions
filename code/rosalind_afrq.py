# ^_^ coding:utf-8 ^_^

"""
Counting Disease Carriers
url: http://rosalind.info/problems/afrq/

Given: An array A for which A[k] represents the proportion of homozygous recessive individuals for the k-th Mendelian factor in a diploid population. Assume that the population is in genetic equilibrium for all factors.
Return: An array B having the same length as A in which B[k] represents the probability that a randomly selected individual carries at least one copy of the recessive allele for the k-th factor.
"""

import numpy as np

with open("../data/rosalind_afrq.txt", "r") as f:
    A = map(float, f.readline().strip().split(" "))

for i in A:
    y = np.sqrt(i)
    x = 1-y
    print(2*y*x+y*y, end=" ")
print()
