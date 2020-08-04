# ^_^ coding:utf-8 ^_^

"""
Edit Distance
url: http://rosalind.info/problems/edit/

Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).
Return: The edit distance dE(s,t).
"""

from Bio import SeqIO

def EditDistance(s, t):
    """
    :type s: str
    :type t: str
    """
    n = len(s)
    m = len(t)
    
    # s or t is empty
    if n * m == 0:
        return n + m
    
    # DP
    D = [ [0] * (m + 1) for _ in range(n + 1)]
    
    # Initializes the edge value
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    
    # calculate DP
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            left = D[i - 1][j] + 1
            down = D[i][j - 1] + 1
            left_down = D[i - 1][j - 1] 
            if s[i - 1] != t[j - 1]:
                left_down += 1
            D[i][j] = min(left, down, left_down)
    
    return D[n][m]

if __name__ == "__main__":
    # load data
    seq_name, seq_string = [], []
    with open("../data/rosalind_edit.txt", "r") as fa:
        for seq_record in SeqIO.parse(fa, "fasta"):
            seq_name.append(seq_record.name)
            seq_string.append(str(seq_record.seq))
    # print(seq_name, seq_string)
    s, t = seq_string
    print(EditDistance(s, t))
