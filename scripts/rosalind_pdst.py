# coding: utf-8
# creating a distance matrix
def read_fasta(file):
	f = open(file, 'r')
	seq = {}
	seqname = []
	for line in f:
		if line.startswith('>'):
			name = line.strip()
			seqname.append(name)
			seq[name] = ''
		else:
			seq[name] += line.strip('\n')
	return seq, seqname

# print read_fasta('C:/Users/310272293/Desktop/rosalind_pdst.txt')
def p_distance(s1, s2):
	n = len(s1)
	m = 0
	for i in range(n):
		if s1[i] != s2[i]:
			m += 1
	return '%.5f'% (float(m)/n)
# print p_distance('TTTCCATTTA', 'GATTCATTTC')

def dis_matrix(file):
	s, sn = read_fasta(file)
	# print sn
	for i in sn:
		for j in sn:
			print p_distance(s[i],s[j]),
		print '\n'


# dis_matrix('C:/Users/310272293/Desktop/rosalind_pdst.txt')