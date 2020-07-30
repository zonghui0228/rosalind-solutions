# ^_^ coding:utf-8 ^_^

"""
RNA Splicing
url: http://rosalind.info/problems/splc/

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
"""

from Bio import SeqIO

coding_table = {
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 
    'TTT': 'F', 'TTC': 'F',
    'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'TAT': 'Y', 'TAC': 'Y',
    'TGT': 'C', 'TGC': 'C',
    'TGG': 'W', 
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
    'ATG': 'M', 
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 
    'AAT': 'N', 'AAC': 'N', 
    'AAA': 'K', 'AAG': 'K',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    'TAA': 'end', 'TAG': 'end', 'TGA': 'end'
}


def RNA_splicing(dna_string, introns):
    for intron in introns:
        dna_string = dna_string.replace(intron, "")
    protein_string  = ""
    for i in range(0, len(dna_string)-2, 3):
        if coding_table[dna_string[i:i+3]] == "end":
            break
        protein_string += coding_table[dna_string[i:i+3]]
    return protein_string


if __name__ == "__main__":
    # load data
    seq_name, seq_string = [], []
    with open ("../data/rosalind_splc.txt",'r') as fa:
        for seq_record  in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))
    # print(seq_string)
    dna_string, introns = seq_string[0], seq_string[1:]
    rna_string = RNA_splicing(dna_string, introns)
    print(rna_string)
