# ^_^ coding:utf-8 ^_^

"""
Majority Element
url: http://rosalind.info/problems/maj/

Given: A positive integer k≤20, a positive integer n≤104, and k arrays of size n containing positive integers not exceeding 105.
Return: For each array, output an element of this array occurring strictly more than n/2 times if such element exists, and "-1" otherwise.
"""

with open("../data/rosalind_maj.txt", "r") as f:
    k, n = map(int, f.readline().strip().split())
    A = [line.strip().split() for line in f]

for i in range(k):
    element_count = [A[i].count(A[i][j]) > n/2 for j in range(n)]
    # print(element_count)
    if any(element_count):
        print(A[i][element_count.index(True)], end=" ")
    else:
        print("-1", end=" ")
