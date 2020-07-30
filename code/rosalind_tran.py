# ^_^ coding:utf-8 ^_^

"""
Transitions and Transversions
url: http://rosalind.info/problems/tran/

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
Return: The transition/transversion ratio R(s1,s2).
"""

from Bio import SeqIO

transition = [('A', 'G'), ('T', 'C'), ('C', 'T'), ('G', 'A')]
transversions = [('A', 'T'), ('A', 'C'), ('T', 'A'), ('T', 'G'), ('C', 'A'), ('C', 'G'), ('G', 'T'), ('G', 'C')]

seq_name, seq_string = [], []
with open ("../data/rosalind_tran.txt",'r') as fa:
    for seq_record  in SeqIO.parse(fa,'fasta'):
        seq_name.append(str(seq_record.name))
        seq_string.append(str(seq_record.seq))

transition_c, transversions_c = 0, 0
s1, s2 = seq_string

for i in range(len(s1)):
    if (s1[i], s2[i]) in transition:
        transition_c += 1
    if (s1[i], s2[i]) in transversions:
        transversions_c += 1
print(transition_c/transversions_c)
