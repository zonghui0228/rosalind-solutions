# ^_^ coding:utf-8 ^_^

"""
Edit Distance Alignment
url: http://rosalind.info/problems/edta/

Given: Two protein strings s and t in FASTA format (with each string having length at most 1000 aa).
Return: The edit distance dE(s,t) followed by two augmented strings s′ and t′ representing an optimal alignment of s and t.
"""

import pprint
from Bio import SeqIO

def EditDistanceAlignment(s, t):
    m, n = len(s), len(t)
    if m*n==0:
        return m+n
    DP = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        DP[i][0] = i
    for j in range(n+1):
        DP[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            left = DP[i-1][j] + 1
            down = DP[i][j-1] + 1
            left_down = DP[i-1][j-1]
            if s[i-1] != t[j-1]:
                left_down += 1
            DP[i][j] = min(left, down, left_down)
    # pprint.pprint(DP)
    edit_distance = DP[m][n]
    print(edit_distance)

    s_, t_ = "", ""
    i, j = 0, 0
    i, j = len(s), len(t)
    while (i>0 and j>0):
        left = DP[i][j-1]
        top = DP[i-1][j]
        left_top = DP[i-1][j-1]
        min_ = min(left, top, left_top)
        if DP[i][j]==min_:
            s_ = s[i-1]+s_
            t_ = t[j-1]+t_
            i -= 1
            j -= 1
        else:
            if (min_==left and min_==top) or (min_!=left and min_!=top):
                s_ = s[i-1]+s_
                t_ = t[j-1]+t_
                i -= 1
                j -= 1
            elif min_!=left and min_==top:
                s_ = s[i-1]+s_
                t_ = "-"+t_
                i -= 1
            elif min_==left and min_!=top:
                s_ = "-"+s_
                t_ = t[j-1]+t_
                j -= 1
    print(s_)
    print(t_)
    return DP

if __name__ == "__main__":
    seq_name, seq_string = [], []
    with open("../data/rosalind_edta.txt", "r") as fa:
        for seq_record in SeqIO.parse(fa, "fasta"):
            seq_name.append(seq_record.name)
            seq_string.append(str(seq_record.seq))
    s, t = seq_string
    res = EditDistanceAlignment(s, t)
