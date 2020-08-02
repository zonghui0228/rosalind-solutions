# ^_^ coding:utf-8 ^_^

"""
Finding a Shared Spliced Motif
url: http://rosalind.info/problems/lcsq/

Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.
Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)
"""

from Bio import SeqIO

def longestCommonSubsequence(s, t):
    # 构建 DP table 和 base case
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # 进行状态转移
    for i, x in enumerate(s):
        for j, y in enumerate(t):
            if x == y:
                # 找到一个 lcs 中的字符
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    
    # Finding a Shared Spliced Motif
    longest_common_subsequence = ""
    while m*n!=0:
        if dp[m][n] == dp[m-1][n]:
            m -= 1
        elif dp[m][n] == dp[m][n-1]:
            n -= 1
        else:
            longest_common_subsequence += s[m-1]
            m -= 1
            n -= 1
    # print(dp)
    print(longest_common_subsequence)
    return longest_common_subsequence

if __name__ == "__main__":
    # load data
    seq_name, seq_string = [], []
    with open("rosalind_lcsq.txt", "r") as fa:
        for seq_record in SeqIO.parse(fa, "fasta"):
            seq_name.append(seq_record.name)
            seq_string.append(str(seq_record.seq))
    s, t = seq_string
    longestCommonSubsequence(s, t)
