# ^_^ coding:utf-8 ^_^

"""
Find the Length of a Longest Path in a Manhattan-like Grid
url: http://rosalind.info/problems/ba5b/

Given: Integers n and m, followed by an n × (m+1) matrix Down and an (n+1) × m matrix Right. The two matrices are separated by the "-" symbol.
Return: The length of a longest path from source (0, 0) to sink (n, m) in the n × m rectangular grid whose edges are defined by the matrices Down and Right.
"""

def LongestPath(n, m, down, right):
    result = [[0] * (m+1) for i in range(n+1)]
    for i in range(1,n+1):
        result[i][0] = result[i-1][0] + down[i-1][0]
    for j in range(1,m+1):
        result[0][j] = result[0][j-1] + right[0][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            result[i][j] = max(result[i-1][j] + down[i-1][j], result[i][j-1] + right[i][j-1])
    return result[n][m]

if __name__ == "__main__":
    with open("../data/rosalind_ba5b.txt", "r") as f:
        n, m = map(int, f.readline().strip().split())
        down = [[int(i) for i in f.readline().strip().split()] for i in range(n)]
        f.readline()
        right = [[int(i) for i in f.readline().strip().split()] for i in range(n+1)]
    print(LongestPath(n,m,down,right))
