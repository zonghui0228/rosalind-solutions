# ^_^ coding:utf-8 ^_^

"""
k-Mer Composition
url: http://rosalind.info/problems/kmer/

Given: A DNA string s in FASTA format (having length at most 100 kbp).
Return: The 4-mer composition of s.
"""

from Bio import SeqIO
import itertools

# load data
seq_name, seq_string = [], []
with open ("../data/rosalind_kmer.txt",'r') as fa:
    for seq_record in SeqIO.parse(fa,'fasta'):
        seq_name.append(str(seq_record.name))
        seq_string.append(str(seq_record.seq))

string = seq_string[0]
kmers = ["".join(x) for x in (itertools.product('ACGT', repeat = 4))]
seq = {i:0 for i in kmers}

for i in range(len(string) - 4 + 1):
    seq[string[i:i+4]] += 1
for i in kmers:
    print(seq[i], end=" ")
