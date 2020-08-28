# ^_^ coding:utf-8 ^_^

"""
Find a Profile-most Probable k-mer in a String
url: http://rosalind.info/problems/ba2c/

Given: A string Text, an integer k, and a 4 × k matrix Profile.
Return: A Profile-most probable k-mer in Text. (If multiple answers exist, you may return any one
"""

def ProbableKmer(string, matrix):
    probable = 1
    for i in range(len(string)):
        if string[i] == 'A':
            probable *= matrix[0][i]
        if string[i] == 'C':
            probable *= matrix[1][i]
        if string[i] == 'G':
            probable *= matrix[2][i]
        if string[i] == 'T':
            probable *= matrix[3][i]
    return probable

def FindProfileMostProbableKmer(string, k, matrix):
    seq = {}
    for i in range(len(string) - k + 1):
        seq[string[i:i + k]] = ProbableKmer(string[i:i + k], matrix)
    max_key = sorted(seq.items(), key=lambda x:x[1], reverse=True)[0][0]
    return max_key

if __name__ == "__main__":
    # string = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
    # k = 5
    # matrix = [[0.2, 0.2, 0.3, 0.2, 0.3], [0.4, 0.3, 0.1, 0.5, 0.1], [0.3, 0.3, 0.5, 0.2, 0.4], [0.1, 0.2, 0.1, 0.1, 0.2]]
    with open("../data/rosalind_ba2c.txt", "r") as f:
        string = f.readline().strip()
        k = int(f.readline().strip())
        matrix =[[float(l) for l in line.strip().split()] for line in f]
    print(FindProfileMostProbableKmer(string, k, matrix))