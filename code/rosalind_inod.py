# ^_^ utf-8: ^_^

"""
Counting Phylogenetic Ancestors
url: http://rosalind.info/problems/inod/

Given: A positive integer n (3≤n≤10000).
Return: The number of internal nodes of any unrooted binary tree having n leaves.
"""

with open("../data/rosalind_inod.txt") as f:
    n = int(f.readline().strip())
# n = 4
print("the number of internal nodes is:", n-2)
print("the total number of the tree nodes is:", 2*n-2)
print("the edges of the tree is:", n-1)
