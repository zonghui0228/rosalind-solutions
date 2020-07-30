# ^_^ coding:utf-8 ^_^

"""
Perfect Matchings and RNA Secondary Structures
url: http://rosalind.info/problems/pmch/

Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.
"""

from Bio import SeqIO

def factorial(n):
    f = 1
    for i in range(n):
        f *= (i+1)
    return f

def pmch(s):
    a = s.count('A')
    c = s.count('C')
    print(a, c)
    return factorial(a) * factorial(c)
if __name__ == "__main__":
    # load data
    seq_name, seq_string = [], []
    with open ("../data/rosalind_pmch.txt",'r') as fa:
        for seq_record  in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))
    string = seq_string[0]
    print(pmch(string))
