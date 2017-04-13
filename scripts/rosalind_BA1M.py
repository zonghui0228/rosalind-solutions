# Convert an integer to its corresponding DNA string.

# Given: Integers index and k.

# Return: NumberToPattern(index, k).

def NumberToPattern(index, k):
	bases = ['A', 'C', 'G', 'T']
	pattern = ''
	for i in range(k):
		pattern += bases[index % 4]
		index = index // 4
	return pattern[::-1]

# print NumberToPattern(45, 4)
