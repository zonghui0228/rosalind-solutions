# ^_^ coding:utf-8 ^_^

"""
Counting Inversions
url: http://rosalind.info/problems/inv/

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.
Return: The number of inversions in A.
"""

def MergeSortCountInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]
        a, ai = MergeSortCountInversions(a)
        b, bi = MergeSortCountInversions(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a)-i)
    c += a[i:]
    c += b[j:]
    return c, inversions

if __name__ == "__main__":
    with open("../data/rosalind_inv.txt", "r") as f:
        n = int(f.readline().strip())
        A = [int(i) for i in f.readline().strip().split()]
    arr, inv_count = MergeSortCountInversions(A)
    print(inv_count)
