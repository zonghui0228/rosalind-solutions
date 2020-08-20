# ^_^ coding:utf-8 ^_^

"""
Quick Sort
url: http://rosalind.info/problems/qs/

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.
Return: A sorted array A[1..n].
"""

def partition(arr, low, high):
    i = low-1
    for j in range(low, high):
        if arr[j] <= arr[high]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    return arr

if __name__ == "__main__":
    with open("../data/rosalind_qs.txt", "r") as f:
        n = int(f.readline().strip())
        A = [int(i) for i in f.readline().strip().split()]
    sortedA = quick_sort(A, 0, n-1)
    for i in sortedA:
        print(i, end=" ")
        