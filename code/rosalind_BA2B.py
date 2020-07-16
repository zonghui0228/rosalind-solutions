# Find a median string.

# Given: An integer k and a collection of strings Dna.

# Return: A k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern. 
# (If multiple answers exist, you may return any one.)
def MinHammingDistance(pattern, string):
	min_distance = len(pattern)
	for i in range(len(string) - len(pattern) + 1):
		count = 0
		for j in range(len(pattern)):
			if pattern[j] != string[i:i+len(pattern)][j]:
				count += 1
			# print count
		if count < min_distance:
			min_distance = count
	return min_distance

print MinHammingDistance('GAC', 'CGTCAGCGCCTG')



def FindMedianString(k, dna):
	from rosalind_BA1K import GenerateArray
	pattern = GenerateArray(k)
	# print kmers_array
	distance_of_pattern_dna = {}
	min_string = len(dna) * len(pattern)
	for i in pattern:
		# distance_of_patterntext[i] = ''
		sum_distance = 0
		for j in range(len(dna)):
			sum_distance += MinHammingDistance(i, dna[j])
		distance_of_pattern_dna[i] = sum_distance
		if sum_distance < min_string:
			min_string = sum_distance
	print distance_of_pattern_dna
	print min_string
	for t in distance_of_pattern_dna.keys():
		if distance_of_pattern_dna[t] == min_string:
			print t

# fp = open("rosalind_BA2B.txt", 'r')
# dna = []
# for line in fp:
# 	dna.append(line.strip('\n'))
# k = int(dna[0])
# dna.remove(dna[0])
# FindMedianString(k, dna)