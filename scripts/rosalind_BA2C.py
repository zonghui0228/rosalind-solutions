# Find a Profile-most probable k-mer in a string.

# Given: A string Text, an integer k, and a 4 * k matrix Profile.

# Return: A Profile-most probable k-mer in Text. (If multiple answers exist, you may return any one.)

def ProbableKmer(string, matrix):
	# the order of dnastring is ATGC
	probable = 1
	for i in range(len(string)):
		if string[i] == 'A':
			probable = probable * matrix[0][i]
		if string[i] == 'C':
			probable = probable * matrix[1][i]
		if string[i] == 'G':
			probable = probable * matrix[2][i]
		if string[i] == 'T':
			probable = probable * matrix[3][i]
	return probable

def FindProfileMostProbableKmer(string, k, matrix):
	seq = {}
	for i in range(len(string) - k + 1):
		seq[string[i:i + k]] = ProbableKmer(string[i:i + k], matrix)
	# print seq
	# print max(seq.values())
	for i in seq.keys():
		if seq[i] == max(seq.values()):
			return i



# string = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
# k = 5
# matrix = [[0.2, 0.2, 0.3, 0.2, 0.3], [0.4, 0.3, 0.1, 0.5, 0.1], [0.3, 0.3, 0.5, 0.2, 0.4], [0.1, 0.2, 0.1, 0.1, 0.2]]
# print ProbableKmer('ATATA', matrix)
# FindProfileMostProbableKmer(string, k, matrix)



