# Given: A DNA string Text and an integer k.
# Return: The frequency array of k-mers in Text.

def GenerateArray(k):
	bases = ['A', 'C', 'G', 'T']
	array = ['A', 'C', 'G', 'T']
	for n in range(k - 1):
		karray = []
		for i in array:
			for j in bases:
				karray.append(i + j)
				array = karray
	return array
# print GenerateArray(7)


def ComputingFrequencyArray(string, k):
	from rosalind_BA1A import patterncount
	for i in GenerateArray(k):
		print patterncount(string, i),

# string = 'ACGCGGCTCTGAAA'
# k = 2
# ComputingFrequencyArray(string, k)