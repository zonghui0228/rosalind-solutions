# ^_^ coding:utf-8 ^_^

"""
Counting DNA Nucleotides
url: http://rosalind.info/problems/dna/

Given: A DNA string  of length at most 1000 nt
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in
"""

def count_DNA(string):
    countA = string.count("A")
    countC = string.count("C")
    countG = string.count("G")
    countT = string.count("T")
    return countA, countC, countG, countT

if __name__ == "__main__":
    with open("../data/rosalind_dna.txt", 'r') as f:
        string = f.readline().strip()
        countA, countC, countG, countT = count_DNA(string)
        print(countA, countC, countG, countT)
