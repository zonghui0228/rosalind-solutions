# ^_^ coding:utf-8 ^_^

"""
Median
url: http://rosalind.info/problems/med/

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105, a positive number k≤n.
Return: The k-th smallest element of A.
"""

def Median(n, A, k):
    v = n//2
    SL, SV, SR = [], [], []
    for i in range(n):
        if A[i] < A[v]: SL.append(A[i])
        if A[i] == A[v]: SV.append(A[i])
        if A[i] > A[v]: SR.append(A[i])
    if k <= len(SL):
        Median(len(SL), SL, k)
    if len(SL) < k and k <=len(SL)+len(SV):
        print(A[v])
        return A[v]
    if k > len(SL)+len(SV):
        Median(len(SR), SR, k-len(SL)-len(SV))

if __name__ == "__main__":
    with open("../data/rosalind_med.txt", "r") as f:
        n = int(f.readline().strip())
        A = [int(i) for i in f.readline().strip().split()]
        k = int(f.readline().strip())
    res = Median(n, A, k)
    