# ^_^ coding:utf-8 ^_^

"""
Generate the Frequency Array of a String
url: http://rosalind.info/problems/ba1k/

Given: A DNA string Text and an integer k.
Return: The frequency array of k-mers in Text.
"""

def GenerateArray(k):
    bases = ['A', 'C', 'G', 'T']
    array = bases
    for n in range(k-1):
        array = [i+j for i in array for j in bases]
    return array

def PatternCount(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

def ComputingFrequencyArray(text, k):
    k_mers = GenerateArray(k)
    for pattern in k_mers:
        print(PatternCount(text, pattern), end=" ")

if __name__ == "__main__":
    # text = 'ACGCGGCTCTGAAA'
    # k = 2
    with open("../data/rosalind_ba1k.txt", "r") as f:
        text = f.readline().strip()
        k = int(f.readline().strip())
    ComputingFrequencyArray(text, k)