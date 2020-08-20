# ^_^ coding:utf-8 ^_^

"""
2SUM
url: http://rosalind.info/problems/2sum/

Given: A positive integer k≤20, a positive integer n≤104, and k arrays of size n containing integers from −105 to 105.
Return: For each array A[1..n], output two different indices 1≤p<q≤n such that A[p]=−A[q] if exist, and "-1" otherwise.
"""

def two_sum(a, target=0):
    tmp_dict = {}
    for i in range(len(a)):
        if a[i] in tmp_dict:
            print(tmp_dict[a[i]] + 1, i + 1)
            return (tmp_dict[a[i]]+1, i+1)
        else:
            tmp_dict[target-a[i]] = i
    print(-1)
    return -1

if __name__ == "__main__":
    with open("../data/rosalind_2sum.txt", "r") as f:
        k, n = map(int, f.readline().strip().split())
        A = [[int(i) for i in line.strip().split()] for line in f]
    for i in range(k):
        r = two_sum(A[i])
