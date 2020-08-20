# ^_^ coding:utf-8 ^_^

"""
2SUM
url: http://rosalind.info/problems/2sum/

Given: A positive integer k≤20, a positive integer n≤104, and k arrays of size n containing integers from −105 to 105.
Return: For each array A[1..n], output two different indices 1≤p<q≤n such that A[p]=−A[q] if exist, and "-1" otherwise.
"""

with open("../data/rosalind_2sum.txt", "r") as f:
    k, n = map(int, f.readline().strip().split())
    A = [[int(i) for i in line.strip().split()] for line in f]

for i in range(k):
    a = A[i]
    for p in range(n-1):
        stop = False
        for q in range(p+1, n):
            if a[p] == -a[q]:
                print(p+1, q+1)
                stop = True
                break
        if stop:
            break
    if not stop:
        print("-1")
