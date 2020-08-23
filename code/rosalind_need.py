# ^_^ coding:utf-8 ^_^

"""
Pairwise Global Alignment
url: http://rosalind.info/problems/need/

Given: Two GenBank IDs.
Return: The maximum global alignment score between the DNA strings associated with these IDs.
"""

from Bio import Entrez, SeqIO, pairwise2

with open("../data/rosalind_need.txt", "r") as f:
    genbank_ids = ", ".join(f.readline().strip().split())
Entrez.email = "**@******"
handle = Entrez.efetch(db="nucleotide", id=[genbank_ids], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
print(pairwise2.align.globalms(records[0].seq, records[1].seq, 5, -4, -10, -1)[0][2])

# https://biopython.org/DIST/docs/api/Bio.pairwise2-module.html
# https://github.com/zonghui0228/Rosalind-Solutions/blob/master/code/rosalind_need.py
