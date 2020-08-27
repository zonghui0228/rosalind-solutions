# ^_^ coding:utf-8 ^_^

"""
Find Patterns Forming Clumps in a String
url: http://rosalind.info/problems/ba1e/

Given: A string Genome, and integers k, L, and t.
Return: All distinct k-mers forming (L, t)-clumps in Genome.
"""

def clump_finding(string, k, L, t):
    res = []
    for i in range(len(string)-L+1):
        for j in range(i,i+L-k):
            if string[i:i+L].count(string[j:j+k]) == t:
                res.append(string[j:j+k])
    res = list(set(res))
    return res

if __name__ == "__main__":
    # s = 'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'
    # k, L, t = 5, 75, 4

    with open("../data/rosalind_ba1e.txt", "r") as f:
        s = f.readline().strip()
        k, L, t = map(int, f.readline().strip().split())
        
    res = clump_finding(s, k, L, t)
    print(" ".join(res))