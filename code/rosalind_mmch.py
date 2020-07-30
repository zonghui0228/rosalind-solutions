# ^_^ coding:utf-8 ^_^

"""
# Maximum Matchings and RNA Secondary Structures
url: http://rosalind.info/problems/mmch/

Given: An RNA string s of length at most 100.
Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s.
"""

import numpy as np
np.set_printoptions(suppress=True)
from Bio import SeqIO

def factorial(n1, n2):
    s = 1
    for i in range(n1, n2, 1):
        s *= (i+1)
    return s

# load data
seq_name, seq_string = [], []
with open("../data/rosalind_mmch.txt", "r") as fa:
    for seq_record in SeqIO.parse(fa, "fasta"):
        seq_name.append(str(seq_record.name))
        seq_string.append(str(seq_record.seq))
s = seq_string[0]

a, c, u, g = s.count('A'), s.count('C'), s.count('U'), s.count('G')
# print(a, c, u, g)

if a <= u:
    p = factorial(u-a, u)
if a > u:
    p = factorial(a-u, a)
if c <= g:
    q = factorial(g-c, g)
if c > g:
    q = factorial(c-g, c)

print(p*q)
