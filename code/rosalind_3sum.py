# ^_^ coding:utf-8 ^_^

"""
3SUM
url: http://rosalind.info/problems/3sum/

Given: A positive integer k≤20, a postive integer n≤104, and k arrays of size n containing integers from −105 to 105.
Return: For each array A[1..n], output three different indices 1≤p<q<r≤n such that A[p]+A[q]+A[r]=0 if exist, and "-1" otherwise."""

def two_sum(a, target2=0):
    tmp_dict = {}
    for i in range(len(a)):
        if a[i] in tmp_dict:
            return (tmp_dict[a[i]]+1, i+1)
        else:
            tmp_dict[target2-a[i]] = i
    return -1

def three_sum(a, target3=0):
    for i in range(len(a)):
        res = two_sum(a[i+1:], target2=target3-a[i])
        if res != -1:
            print(i+1, i+1+res[0], i+1+res[1])
            return (i+1, i+1+res[0], i+1+res[1])
    print(-1)
    return -1

if __name__ == "__main__":
    with open("../data/rosalind_3sum.txt", "r") as f:
        k, n = map(int, f.readline().strip().split())
        A = [[int(i) for i in line.strip().split()] for line in f]
    for i in range(k):
        r = three_sum(A[i])
