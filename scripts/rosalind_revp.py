# Locating Restriction Sites
# A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, 
# GCATGC is a reverse palindrome because its reverse complement is GCATGC

# Sample Dataset
# >Rosalind_24
# TCAATGCATGCGGGTCTATATGCAT

# Sample Output
# 4 6
# 5 4
# 6 6
# 7 4
# 17 4
# 18 4
# 20 6
# 21 4
def read_fasta(file):
	fp = open(file, 'r')
	seq = {}
	s = ''
	for line in fp:
		if line.startswith('>'):
			name = line.strip('\n')
			name = name.strip('>')
			seq[name] = ''
		else:
			seq[name] += line.strip('\n')
	# print seq
	for i in seq.keys():
		s = seq[i]
	return s
# print read_fasta("rosalind_revp.txt")
def switch(s):
	s = s[::-1]
	# print s
	switch_s = ''
	for i in range(len(s)):
		if s[i] == 'A':
			switch_s += 'T'
		elif s[i] == 'T':
			switch_s += 'A'
		elif s[i] == 'G':
			switch_s += 'C'
		elif s[i] == 'C':
			switch_s += 'G'
	return switch_s
# print switch('TGCA')	

def palindrome(file):
	s1 = read_fasta(file)
	# print s1
	for i in range(len(s1)):
		for j in range(4,13,1):
			if s1[i:i+j] == switch(s1[i:i+j]) and (i+j <= len(s1)):
				print i+1, j
# palindrome("rosalind_revp.txt")
