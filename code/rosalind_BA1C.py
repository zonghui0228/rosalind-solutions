# ^_^ coding:utf-8 ^_^

"""
Find the Reverse Complement of a String
url: http://rosalind.info/problems/ba1c/

Given: A DNA string Pattern.
Return: Pattern, the reverse complement of Pattern.
"""

from Bio import Seq

def ReverseComplement(dna):
	reverse_dna = Seq.reverse_complement(dna)
	return reverse_dna

if __name__ == "__main__":
	with open("../data/rosalind_ba1c.txt", "r") as f:
		dna = f.readline().strip()
	reverse_dna = ReverseComplement(dna)
	print(reverse_dna)
