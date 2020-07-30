# ^_^ coding: utf-8 ^_^

"""
3-Way Partition
url: http://rosalind.info/problems/par3/

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.
Return: An array B[1..n] such that it is a permutation of A and there are indices 1≤q≤r≤n such that B[i]<A[1] for all 1≤i≤q−1, B[i]=A[1] for all q≤i≤r, and B[i]>A[1] for all r+1≤i≤n.
"""

def partition3(array):
    new_array, left_array, right_array = [], [], []
    new_array.append(array[0])
    for i in range(1, len(array)):
        if array[i] < array[0]:
            left_array.append(array[i])
        elif array[i] == array[0]:
            new_array.append(array[i])
        else:
            right_array.append(array[i])
    new_array = left_array + new_array + right_array
    return new_array    

if __name__ == '__main__':
    with open("../data/rosalind_par3.txt", "r") as f:
        n = int(f.readline().strip())
        A = [int(i) for i in f.readline().strip().split(" ")]
    results = partition3(A)
    for r in results:
        print(r, end=" ")
    print()
