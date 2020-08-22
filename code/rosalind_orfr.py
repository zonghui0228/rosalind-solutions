# ^_^ coding:utf-8 ^_^

"""
Finding Genes with ORFs
url: http://rosalind.info/problems/orfr/

Given: A DNA string s of length at most 1 kbp.
Return: The longest protein string that can be translated from an ORF of s. If more than one protein string of maximum length exists, then you may output any solution.
"""

from Bio.Seq import Seq
from Bio import SeqIO

def gene_ORFs(s):
    s = Seq(s)
    s_reverse = s.reverse_complement()
    proteins = []
    proteins.extend(str(s.translate()).split("*"))
    proteins.extend(str(s[1:].translate()).split("*"))
    proteins.extend(str(s[2:].translate()).split("*"))
    proteins.extend(str(s_reverse.translate()).split("*"))
    proteins.extend(str(s_reverse[1:].translate()).split("*"))
    proteins.extend(str(s_reverse[2:].translate()).split("*"))

    orfs = sorted([i[i.find("M"):] for i in proteins if "M" in i], key= lambda x: len(x), reverse=True)
    print(orfs[0])
    return orfs

if __name__ == "__main__":
    with open("../data/rosalind_orfr.txt", "r") as f:
        dna = f.readline().strip()
    gene_ORFs(dna)