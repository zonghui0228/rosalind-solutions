# ^_^ coding:utf-8 ^_^

"""
Implement MotifEnumeration
url: http://rosalind.info/problems/ba2a/

Given: Integers k and d, followed by a collection of strings Dna.
Return: All (k, d)-motifs in Dna.
"""

def neighbour(pattern, mismatch, words):
    if mismatch == 0:
        words.add(pattern)
    else:
        bases = ['A', 'T', 'C', 'G']
        for i in range(len(pattern)):
            for j in range(len(bases)):
                new_pattern = pattern[:i] + bases[j] + pattern[i+1:]
                if mismatch <= 1:
                    words.add(new_pattern)
                else:
                    neighbour(new_pattern, mismatch-1, words)

def MotifEnumeration(dna, k, d):
    patterns = []
    for n in range(len(dna)):
        pattern = set()
        for i in range(len(dna[n]) - k + 1):
            kmerspattern = set()
            neighbour(dna[n][i:i + k], d, kmerspattern)
            for words in kmerspattern:
                pattern.add(words)
        for j in pattern:
            patterns.append(j)
    motifpattern = []
    for element in patterns:
        if patterns.count(element) == len(dna):
            motifpattern.append(element)
    motifpattern = list(set(motifpattern))
    return motifpattern

if __name__ == "__main__":
    with open("../data/rosalind_ba2a.txt", "r") as f:
        k, d = map(int, f.readline().strip().split())
        dna = [line.strip() for line in f]
    for i in MotifEnumeration(dna, k, d):
        print(i)