# ^_^ coding:utf-8 ^_^

"""
Sex-Linked Inheritance
url: http://rosalind.info/problems/sexl/

Given: An array A of length n for which A[k] represents the proportion of males in a population exhibiting the k-th of n total recessive X-linked genes. Assume that the population is in genetic equilibrium for all n genes.
Return: An array B of length n in which B[k] equals the probability that a randomly selected female will be a carrier for the k-th gene.
"""

with open("../data/rosalind_sexl.txt", "r") as f:
    A = map(float, f.readline().strip().split())
for p in A:
    print(2*p*(1-p), end=" ")
print()
