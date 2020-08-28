# ^_^ coding:utf-8 ^_^

"""
Implement GreedyMotifSearch
url: http://rosalind.info/problems/ba2d/

Given: Integers k and t, followed by a collection of strings Dna.
Return: A collection of strings BestMotifs resulting from running GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.
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

# Profile-most probable k-mer in the i-th string in Dna
def FindProfileMostProbableKmer(string, k, matrix):
    seq = {}
    for i in range(len(string) - k + 1):
        seq[string[i:i + k]] = ProbableKmer(string[i:i + k], matrix)
    max_key = sorted(seq.items(), key=lambda x:x[1], reverse=True)[0][0]
    return max_key

# Score(Motifs)
def Score(Motifs):
    score = 0
    for i in range(len(Motifs[0])):
        j = [motif[i] for motif in Motifs]
        score += (len(j) - max(j.count("A"), j.count("C"), j.count("T"), j.count("G")))
    return score

def GreedyMotifSearch(Dna, k, t):
    # BestMotifs ← motif matrix formed by first k-mers in each string from Dna
    BestMotifs = [dna[:k] for dna in Dna]
    # for each k-mer Motif in the first string from Dna
    for k_mer in [Dna[0][i:i+k] for i in range(len(Dna[0])-k+1)]:
        # Motif1 ← Motif
        Motifs = [k_mer]
        # for i = 2 to t
        for i in range(1, t):
            # form Profile from motifs Motif1, …, Motifi - 1
            motifs = Motifs[:i]
            # Motifi ← Profile-most probable k-mer in the i-th string in Dna
            matrix = []
            for nar in ["A", "C", "G", "T"]:
                mat = []
                for j in range(k):
                    mm = [m[j] for m in motifs]
                    mat.append(mm.count(nar)/len(motifs))
                matrix.append(mat)
            # Motifs ← (Motif1, …, Motift)    
            Motifs.append(FindProfileMostProbableKmer(Dna[i], k, matrix))
        # print(Motifs)
        # if Score(Motifs) < Score(BestMotifs), BestMotifs ← Motifs
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

if __name__ == "__main__":
    with open("../data/rosalind_ba2d.txt", "r") as f:
        k, t = map(int, f.readline().strip().split())
        Dna = [line.strip() for line in f]
    # print(k,t,Dna)
    BestMotifs = GreedyMotifSearch(Dna, k ,t)
    print("\n".join(BestMotifs))