# ^_^ coding:utf-8 ^_^

"""
Building a Heap
url: http://rosalind.info/problems/hea/

Given: A positive integer n≤105 and array A[1..n] of integers from −105 to 105.
Return: A permuted array A satisfying the binary max heap property: for any 2≤i≤n, A[⌊i/2⌋]≥A[i].
"""

def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1 # left = 2*i + 1 
    r = 2 * i + 2 # right = 2*i + 2 

    # If left child is larger than root 
    if l < n and arr[l] > arr[largest]:
        largest = l 
  
    # If right child is larger than largest so far 
    if r < n and arr[r] > arr[largest]:
        largest = r
  
    # If largest is not root 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def buildHeap(arr, n): 
    startIdx = n // 2 - 1
    for i in range(startIdx, -1, -1): 
        heapify(arr, n, i)

if __name__ == '__main__': 
    with open("../data/rosalind_hea.txt", "r") as f:
        n = int(f.readline().strip())
        arr = [int(i) for i in f.readline().strip().split()]
    buildHeap(arr, n)
    for i in range(n): 
            print(arr[i], end = " ")
    print()

# reference: https://www.geeksforgeeks.org/building-heap-from-array/