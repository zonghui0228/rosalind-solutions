# ^_^ coding:utf-8 ^_^

"""
Introduction to the Bioinformatics Armory
url: http://rosalind.info/problems/ini/

Given: A DNA string s of length at most 1000 bp.
Return: Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s. Note: You must provide your answer in the format shown in the sample output below.
"""

def ini(dna):
    symbols = ["A", "C", "G", "T"]
    symbols_count = {i:dna.count(i) for i in symbols}
    return symbols_count

if __name__ == "__main__":
    with open("../data/rosalind_ini.txt", "r") as f:
        dna = f.readline().strip()
    symbols_count = ini(dna)
    for k,v in symbols_count.items():
        print(v, end=" ") 