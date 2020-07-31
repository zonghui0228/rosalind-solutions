# ^_^ coding:utf-8 ^_^

""" 
Error Correction in Reads
url: http://rosalind.info/problems/corr/

Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated with a single-nucleotide error. For each read s in the dataset, one of the following applies: s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement); s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).
Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)
"""

from Bio import SeqIO

def hamming_distance(s1, s2):
    return sum([1 if s1[i]!=s2[i] else 0 for i in range(len(s1))])

def error_correct(reads):
    corrections = []
    correct_reads, incorrect_reads = [], []
    reverse_pattern={"A": "T", "T": "A", "C": "G", "G": "C"}

    for r in reads:
        reverse_r = "".join([reverse_pattern[i] for i in r[::-1]])
        if reads.count(r) + reads.count(reverse_r) >= 2:
            correct_reads.append(r)
        else:
            incorrect_reads.append(r)

    for ir in incorrect_reads:
        for cr in correct_reads:
            reverse_cr = "".join([reverse_pattern[i] for i in cr[::-1]])
            if hamming_distance(ir, cr) == 1:
                corrections.append((ir, cr))
                break
            if hamming_distance(ir, reverse_cr) == 1:
                corrections.append((ir, reverse_cr))
                break

    return corrections

if __name__ == "__main__":
    # load data
    seq_name, seq_string = [], []
    with open ("../data/rosalind_corr.txt",'r') as fa:
        for seq_record in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))
    # print(seq_string)
    corrections = error_correct(seq_string)
    for ir, cr in corrections:
        print("{}->{}".format(ir, cr))
