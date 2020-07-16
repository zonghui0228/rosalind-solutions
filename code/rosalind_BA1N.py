# Generate the d-Neighborhood of a String

# Given: A DNA string Pattern and an integer d.
# Return: The collection of strings Neighbors(Pattern, d).
def Neighbors(pattern, d):
	from rosalind_BA1K import GenerateArray
	from rosalind_BA1H import hamming_distance
	array = GenerateArray(len(pattern))
	neighbors = []
	for i in array:
		if hamming_distance(pattern, i) <= d:
			neighbors.append(i)
	return neighbors
# string = 'TTCCCAGCAC'
# d = 3
# for i in Neighbors(string, d):
# 	print i
