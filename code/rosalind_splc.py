# RNA Splicing
def exon(file):
	fp = open(file, 'r')
	seq = {}
	for line in fp:
		if line.startswith('>'):
			name = line.strip('\n')
			name = name.strip('>')
			seq[name] = ''
		else:
			seq[name] += line.strip('\n')
	# print seq
	fp.close()
	max1 = 0
	s1 = ''
	# the old string
	for i in seq.keys():
		if len(seq[i]) > max1:
			max1 = len(seq[i])
			s1 = seq[i]
	# print s1
	list1 = []
	for i in seq.keys():
		if seq[i] != s1:
			list1.append(seq[i])
	# print list1
	for i in list1:
		s1 = s1.replace(i, '')
	# print s1
	return s1
# exon("rosalind_splc.txt")

def coding(s):
	if s == 'TTT' or s == 'TTC':
		return 'F'
	elif s == 'TTA' or s == 'TTG' or s == 'CTT' or s == 'CTC' or s == 'CTA' or s == 'CTG':
		return 'L'
	elif s == 'TCT' or s == 'TCC' or s == 'TCA' or s == 'TCG' or s == 'AGT' or s == 'AGC':
		return 'S'
	elif s == 'TAT' or s == 'TAC':
		return 'Y'
	elif s == 'TGT' or s == 'TGC':
		return 'C'
	elif s == 'TGG':
		return 'W'
	elif s == 'CCT' or s == 'CCC' or s == 'CCA' or s == 'CCG':
		return 'P'
	elif s == 'CAT' or s == 'CAC':
		return 'H'
	elif s == 'CAA' or s == 'CAG':
		return 'Q'
	elif s == 'CGT' or s == 'CGC' or s == 'CGA' or s == 'CGG' or s == 'AGA' or s == 'AGG':
		return 'R'
	elif s == 'ATT' or s == 'ATC' or s == 'ATA':
		return 'I'
	elif s == 'ATG':
		return 'M'
	elif s == 'ACT' or s == 'ACC' or s == 'ACA' or s == 'ACG':
		return 'T'
	elif s == 'AAT' or s == 'AAC':
		return 'N'
	elif s == 'AAA' or s == 'AAG':
		return 'K'
	elif s == 'GTT' or s == 'GTC' or s == 'GTA' or s == 'GTG':
		return 'V'
	elif s == 'GCT' or s == 'GCC' or s == 'GCA' or s == 'GCG':
		return 'A'
	elif s == 'GAT' or s == 'GAC':
		return 'D'
	elif s == 'GAA' or s == 'GAG':
		return 'E'
	elif s == 'GGT' or s == 'GGC' or s == 'GGA' or s == 'GGG':
		return 'G'
	elif s == 'TAA' or s == 'TAG' or s == 'TGA':
		return '~'

def result(sequence):
	s1 = ''
	for i in range(0, len(sequence)-2, 3):
		s1 = s1 + str(coding(sequence[i:i+3]))
	return s1

def splicing(file):
	s = exon(file)
	print s
	t = result(s)
	print t
# splicing("rosalind_splc.txt")