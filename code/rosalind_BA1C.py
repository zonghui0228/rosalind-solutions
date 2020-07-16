# Find the Reverse Complement of a String
def reverse_pattern(s):
	reverse_s = ''
	for i in range(len(s)-1, -1, -1):
		if s[i] == 'A':
			reverse_s += 'T'
		elif s[i] == 'T':
			reverse_s += 'A'
		elif s[i] == 'G':
			reverse_s += 'C'
		elif s[i] == 'C':
			reverse_s += 'G'
	return reverse_s

string = 'AAAACCCGGT'
print reverse_pattern(string)
