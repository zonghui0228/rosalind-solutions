# ^_^ coding:utf-8 ^_^

"""
Find the Most Frequent Words with Mismatches in a String
url: http://rosalind.info/problems/ba1i/

Given: A string Text as well as integers k and d.
Return: All most frequent k-mers with up to d mismatches in Text.
"""

from collections import defaultdict

def neighbour(pattern, mismatch, words):
    bases = ['A', 'T', 'G', 'C']
    for i in range(len(pattern)):
        for j in range(len(bases)):
            new_pattern = pattern[:i] + bases[j] + pattern[i+1:]
            if mismatch <= 1:
                words.add(new_pattern)
            else:
                neighbour(new_pattern, mismatch - 1, words)
def FindMostFrequentWords(text, k, d):
    AllFrequentWords = defaultdict(int)
    for i in range(len(text) - k + 1):
        FrequentWords = set()
        neighbour(text[i:i + k], d, FrequentWords)
        for words in FrequentWords:
            AllFrequentWords[words] += 1
    # print AllFrequentWords
    for t in AllFrequentWords.keys():
        if AllFrequentWords[t] == max(AllFrequentWords.values()):
            print(t, end=" ")

if __name__ == "__main__":
    # text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    # k, d = 4, 1
    with open("../data/rosalind_ba1i.txt", "r") as f:
        text = f.readline().strip()
        k, d = map(int, f.readline().strip().split())
    FindMostFrequentWords(text, k, d)
