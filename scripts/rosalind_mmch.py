# Maximum Matchings and RNA Secondary Structures
# Sample Dataset
# >Rosalind_92
# AUGCUUC
# Sample Output
# 6
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
	u = s.count('U')
	g = s.count('G')
	if a <= u:
		p = factorial(u)/factorial(u-a)
	if a > u:
		p = factorial(a)/factorial(a-u)
	if c <= g:
		q = factorial(g)/factorial(g-c)
	if c > g:
		q = factorial(c)/factorial(c-g)
	print a, c, u, g

	return p * q

# print pmch("test.txt")
