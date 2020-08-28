# ^_^ coding:utf-8 ^_^

"""
Find Frequent Words with Mismatches and Reverse Complements
url: http://rosalind.info/problems/ba1j/

Given: A DNA string Text as well as integers k and d.
Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern) over all possible k-mers.
"""

from collections import defaultdict
from Bio import Seq

def HammingDistance(s1, s2):
    d = sum([1 for i in range(len(s1)) if s1[i]!=s2[i]])
    return d

def ReversePattern(pattern):
    return Seq.reverse_complement(pattern)

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

def FindMostFrequentPattern(text, k, d):
    allfrequentwords = defaultdict(int)
    for i in range(len(text) - k + 1):
        frequentwords = set()
        neighbour(text[i:i + k], d, frequentwords)

        for words in frequentwords:
            allfrequentwords[words] += 1

    for t in allfrequentwords.keys():
        reverse_k = ReversePattern(t)
        for i in range(len(text) - k + 1):
            if HammingDistance(text[i:i + k], reverse_k) <= d:
                allfrequentwords[t] += 1

    result = set()
    for t in allfrequentwords.keys():
        if allfrequentwords[t] == max(allfrequentwords.values()):
            result.add(t)
            result.add(ReversePattern(t))
    for i in result:
        print(i, end=" ")
        
if __name__ == "__main__":
    # text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    # k, d = 4, 1
    with open("../data/rosalind_ba1j.txt", "r") as f:
        text = f.readline().strip()
        k, d = map(int, f.readline().strip().split())
    FindMostFrequentPattern(text, k, d)
