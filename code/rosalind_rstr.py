# ^_^ coding:utf-8 ^_^

"""
Matching Random Motifs
url: http://rosalind.info/problems/rstr/

Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.
Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x (see “Introduction to Random Strings”), then at least one of the strings equals s. We allow for the same random string to be created more than once.
"""

with open("../data/rosalind_rstr.txt", "r") as f:
    N, x = f.readline().strip().split(" ")
    N = int(N)
    x = float(x)
    s = f.readline().strip()

# N = 97698
# x = 0.462550
# s = 'AGATGGCCA'
at = s.count('A') + s.count('T')
gc = s.count('G') + s.count('C')
P_s = pow(x/2, gc) * pow((1-x)/2, at)
print(1 - pow(1 - P_s, N))
