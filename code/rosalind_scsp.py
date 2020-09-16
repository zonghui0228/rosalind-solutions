# ^_^ coding:utf-8 ^_^

"""
Interleaving Two Motifs
url: http://rosalind.info/problems/scsp/

Given: Two DNA strings s and t.
Return: A shortest common supersequence of s and t. If multiple solutions exist, you may output any one.
"""

import pprint

def LCS(s1, s2):
    m, n = len(s1), len(s2)
    DP = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                DP[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                DP[i][j] = DP[i-1][j-1]+1
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])
    # pprint.pprint(DP)

    scs = ""
    i, j = len(s1), len(s2)
    while (i>0 or j>0):
        if DP[i][j] == DP[i-1][j]:
            i -= 1
            scs = s1[i]+scs
        elif DP[i][j] == DP[i][j-1]:
            j -= 1
            scs = s2[j]+scs
        else:
            scs = s1[i-1]+scs
            i -= 1
            j -= 1
    print(scs)
    return DP[m][n]

if __name__ == "__main__":
    with open("../data/rosalind_scsp.txt", "r") as f:
        s1 = f.readline().strip()
        s2 = f.readline().strip()
    res = LCS(s1, s2)