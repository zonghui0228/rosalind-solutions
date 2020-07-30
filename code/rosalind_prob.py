# ^_^ coding:utf-8 ^_^

"""
Introduction to Random Strings
url: http://rosalind.info/problems/prob

Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.
Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.
"""

import math

with open("../data/rosalind_prob.txt", "r") as f:
    s = f.readline().strip()
    A = map(float, f.readline().strip().split(" "))

a = s.count('A') + s.count('T')
c = s.count('C') + s.count('G')
for i in A:
    p = a * math.log((1-i)/2, 10) + c * math.log(i/2, 10)
    print(p, end=" ")
    