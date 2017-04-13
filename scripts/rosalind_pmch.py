# Perfect Matchings and RNA Secondary Structures
# Sample Dataset
# >Rosalind_23
# AGCUAGUCAU
# Sample Output
# 12
def factorial(n):
	s = 1
	for i in range(n):
		s = s * (i+1)
	return s

def pmch(file):
	fp = open(file, 'r')
	seq = {}
	for line in fp:
		if line.startswith('>'):
			line = line.strip('>')
			name = line.strip('\n')
			seq[name] = ''
		else:
			seq[name] += line.strip('\n')
	for i in seq.keys():
		s = seq[i]
	# print s
	a = s.count('A')
	c = s.count('C')
	print a, c
	return factorial(a) * factorial(c)

# print pmch("rosalind_pmch.txt")


