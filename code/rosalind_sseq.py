# ^_^ coding:utf-8 ^_^

"""
Finding a Spliced Motif
url: http://rosalind.info/problems/sseq/

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
"""

from Bio import SeqIO

def find_spliced_motif(s, t):
    position = [0]
    for i in t:
        position.append(s[position[-1]:].index(i) + 1 + position[-1])
        # print(s.index(i))
    for p in position[1:]:
        print(p, end=" ")

if __name__ == "__main__":
    seq_name, seq_string = [], []
    with open ("../data/rosalind_sseq.txt",'r') as fa:
        for seq_record  in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))

    s, t = seq_string[0], seq_string[1]
    find_spliced_motif(s,t)