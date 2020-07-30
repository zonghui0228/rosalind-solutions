# ^_^ coding: utf-8 ^_^

"""
Merge Two Sorted Arrays
url: http://rosalind.info/problems/mer/

Given: A positive integer n≤105 and a sorted array A[1..n] of integers from −105 to 105, a positive integer m≤105 and a sorted array B[1..m] of integers from −105 to 105.
Return: A sorted array C[1..n+m] containing all the elements of A and B.
"""

import linecache

def merge_sort(A, B):
    C = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
	# 最后一项即最大值，在下一步写入
    C += A[i:]
    C += B[j:]
    return C

if __name__ == '__main__':
    with open("../data/rosalind_mer.txt", "r") as f:
        n = int(f.readline())
        A = [int(i) for i in f.readline().strip().split(' ')]
        m = int(f.readline())
        B = [int(i) for i in f.readline().strip().split(' ')]
    C = merge_sort(A, B)
    for i in C:
        print(i, end=" ")
    print()
