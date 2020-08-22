# ^_^ coding:utf-8 ^_^

"""
Data Formats
url: http://rosalind.info/problems/frmt/

Given: A collection of n (n≤10) GenBank entry IDs.
Return: The shortest of the strings associated with the IDs in FASTA format.
"""

from Bio import Entrez, SeqIO

def shortest_entry(entry_ids):
    Entrez.email = "***@*****"
    handle = Entrez.efetch(db="nucleotide", id=[", ".join(entry_ids)], rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))
    print(min(records, key=lambda s: len(s.seq)).format("fasta"))

if __name__ == "__main__":
    with open("../data/rosalind_frmt.txt", "r") as f:
        entry_ids = f.readline().strip().split()
    shortest_entry(entry_ids)