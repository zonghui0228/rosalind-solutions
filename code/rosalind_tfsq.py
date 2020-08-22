# ^_^ coding:utf-8 ^_^

"""
FASTQ format introduction
url: http://rosalind.info/problems/tfsq/

Given: FASTQ file
Return: Corresponding FASTA records
"""

from Bio import SeqIO
fastq_file = "../data/rosalind_tfsq.txt"
fasta_file = "../data/rosalind_tfsq.out.txt"
SeqIO.convert(fastq_file, 'fastq', fasta_file, 'fasta')
