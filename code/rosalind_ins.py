# coding: utf-8

"""
Insertion Sort
url: http://rosalind.info/problems/ins/

Given: A positive integer n≤103 and an array A[1..n] of integers.
Return: The number of swaps performed by insertion sort algorithm on A[1..n].
"""

# 插入排序
# 每次找最小值
# 最坏的情况下复杂度为list长度的平方
def ins(array):
    swap = 0
    for i in range(len(array)):
        k = i
        while k > 0 and array[k] < array[k-1]:
            array[k-1], array[k] = array[k], array[k-1]
            swap += 1
            k -= 1
    # return array 返回排序后的列表
    return swap        # 返回交换次数

if __name__ == "__main__":
    with open('../data/rosalind_ins.txt', 'r') as f:
        f.readline()
        s = [int(i) for i in f. readline().strip().split(' ')]
        print(ins(s))