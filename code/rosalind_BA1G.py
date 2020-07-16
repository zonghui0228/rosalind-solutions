# Compute the Hamming Distance Between Two Strings
def hamming_distance(s1, s2):
	count = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			count += 1
	return count

a = 'GGGCCGTTGGT'
b = 'GGACCGTTGAC'
# print hamming_distance(a, b)