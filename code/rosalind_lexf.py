# Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n <= 10).

# Return: All strings of length that can be formed from the alphabet, ordered lexicographically.


import itertools
fp = open("rosaind_lexf.txt", 'r')
string = fp.readline().split()
n = int(fp.readline().strip())
result = list(itertools.product(string, repeat = n))
print "\n".join(["".join(x) for x in result])