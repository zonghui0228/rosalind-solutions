# Find All Approximate Occurrences of a Pattern in a String
def hamming_distance(s1, s2):
	count = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			count += 1
	return count
def approximate_pattern(pattern, text, d):
	for i in range(len(text)-len(pattern)+1):
		if hamming_distance(pattern, text[i:i+len(pattern)]) <= d:
			print i,

p = 'ATTCTGGA'
t = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC'
d = 3
# approximate_pattern(p, t, d)