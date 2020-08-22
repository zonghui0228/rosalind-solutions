# ^_^ coding:utf-8 ^_^

"""
Complementing a Strand of DNA
url: http://rosalind.info/problems/rvco/

Given: A collection of n (n≤10) DNA strings.
Return: The number of given strings that match their reverse complements.
"""

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def match_reverse(seqs):
    count = 0
    for seq in seqs:
        my_seq = Seq(seq, IUPAC.unambiguous_dna)
        reverse_seq = my_seq.reverse_complement()
        if my_seq == reverse_seq:
            count += 1
    return count

if __name__ == "__main__":
    with open("../data/rosalind_rvco.txt", "r") as f:
        seqs = [str(record.seq) for record in SeqIO.parse(f, "fasta")]
    count = match_reverse(seqs)
    print(count)