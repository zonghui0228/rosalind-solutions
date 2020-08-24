# ^_^ coding:utf-8 ^_^

"""
Heap Sort 
url: http://rosalind.info/problems/hs/

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.
Return: A sorted array A.
"""

def heapify(arr, n, i): 
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]: 
        largest = l
    if r < n and arr[r] > arr[largest]: 
        largest = r
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest); 
  
def buildHeap(arr, n):
    for i in range(n//2 , -1, -1): 
        heapify(arr, n, i)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == '__main__': 
    with open("../data/rosalind_hs.txt", "r") as f:
        n = int(f.readline().strip())
        arr = [int(i) for i in f.readline().strip().split()]
    buildHeap(arr, n)

    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        n -= 1
        heapify(arr, n, 0)

    for i in range(len(arr)): 
            print(arr[i], end = " ")
    print()