# ^_^ coding:utf-8 ^_^

"""
Global Multiple Alignment
url: http://rosalind.info/problems/clus/

Given: Set of nucleotide strings in FASTA format.
Return: ID of the string most different from the others.
"""

from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO

def multiple_align(infile):
    clustalw2_path = "C:\\Program Files (x86)\\ClustalW2\\clustalw2.exe" # path to clustalw2
    clustalw_cline = ClustalwCommandline(clustalw2_path, infile=infile)
    stdout, stderr = clustalw_cline()
    aln = infile.replace(".txt",".aln")
    align = AlignIO.read(aln, "clustal")
    print(align)

if __name__ == "__main__":
    data = "../data/rosalind_clus.txt"
    multiple_align(data)