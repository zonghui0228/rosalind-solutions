# ^_^ coding:utf-8 ^_^

"""
Enumerating k-mers Lexicographically
url: http://rosalind.info/problems/lexf/

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n <= 10).
Return: All strings of length that can be formed from the alphabet, ordered lexicographically.
"""

import itertools

with open("../data/rosalind_lexf.txt", 'r') as f:
    string = f.readline().split()
    n = int(f.readline().strip())
    result = list(itertools.product(string, repeat = n))
    print("\n".join(["".join(x) for x in result]))
    