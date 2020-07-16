# python3


# Given: An RNA string  corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by


def prot(string):
	pattern = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
		   "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
		   "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
		   "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
		   "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
		   "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
		   "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
		   "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
		   "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
		   "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
		   "UAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
		   "UAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
		   "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
		   "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
		   "UGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
		   "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}
	rst = ''.join([pattern[string[i:i+3]] for i in range(0, len(string), 3)])
	return rst[:rst.index("*")]


if __name__ == "__main__":
	with open("../data/rosalind_prot.txt", 'r') as f:
		string = f.readline().strip()
		print(prot(string))



