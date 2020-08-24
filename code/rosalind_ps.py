# ^_^ coding:utf-8 ^_^

"""
Partial Sort
url: http://rosalind.info/problems/ps/

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105, a positive integer k≤1000.
Return: The k smallest elements of a sorted array A.
"""

def heapify(arr, n, i): 
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] < arr[largest]: 
        largest = l
    if r < n and arr[r] < arr[largest]: 
        largest = r
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest); 
  
def buildHeap(arr, n):
    for i in range(n//2 , -1, -1): 
        heapify(arr, n, i)

if __name__ == '__main__': 
    with open("../data/rosalind_ps.txt", "r") as f:
        n = int(f.readline().strip())
        arr = [int(i) for i in f.readline().strip().split()]
        k = int(f.readline().strip())

    for i in range(k):
        buildHeap(arr, n)
        print(arr[0], end=" ")
        arr = arr[1:]
        n = len(arr)
    print()