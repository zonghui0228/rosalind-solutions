# Given: Integers k and d, followed by a collection of strings Dna.

# Return: All (k, d)-motifs in Dna
def MotifEnumeration(dna, k, d):
	patterns = []
	from rosalind_BA1J import neighbour
	# print dna[0]
	for n in range(len(dna)):
		# print n
		pattern = set()
		# print pattern
		# print dna[n]
		for i in range(len(dna[n]) - k + 1):
			
			kmerspattern = set()
			neighbour(dna[n][i:i + k], d, kmerspattern)
			# print kmerspattern
			for words in kmerspattern:
				pattern.add(words)
		# print pattern
		for j in pattern:
			patterns.append(j)
	# print patterns
	motifpattern = []
	for element in patterns:
		if patterns.count(element) == len(dna):
			motifpattern.append(element)
	motifpattern = list(set(motifpattern))
	return motifpattern

# dna = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
# k = 3
# d = 1
# for i in MotifEnumeration(dna, k, d):
# 	print i