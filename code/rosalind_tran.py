# the transition / transversions ratio
# give two dna string of the same length
def read_fasta(file):
	fp = open(file, 'r')
	seq = {}
	for line in fp:
		if line.startswith('>'):
			name = line.strip('>')
			name = name.strip('\n')
			seq[name] = ''
		else:
			seq[name] += line.strip('\n')
	return seq
	fp.close()


def ratio(file):
	seq = read_fasta(file)
	list1 = []
	for i in seq.keys():
		list1.append(seq[i])
	# print list1
	transition = 0.0
	transversions = 0.0
	for i in range(len(list1[0])):
		if list1[0][i] == 'A' and list1[1][i] == 'T':
			transversions += 1
		if list1[0][i] == 'A' and list1[1][i] == 'G':
			transition += 1
		if list1[0][i] == 'A' and list1[1][i] == 'C':
			transversions += 1
		if list1[0][i] == 'T' and list1[1][i] == 'A':
			transversions += 1
		if list1[0][i] == 'T' and list1[1][i] == 'C':
			transition += 1
		if list1[0][i] == 'T' and list1[1][i] == 'G':
			transversions += 1
		if list1[0][i] == 'C' and list1[1][i] == 'A':
			transversions += 1
		if list1[0][i] == 'C' and list1[1][i] == 'T':
			transition += 1
		if list1[0][i] == 'C' and list1[1][i] == 'G':
			transversions += 1
		if list1[0][i] == 'G' and list1[1][i] == 'T':
			transversions += 1
		if list1[0][i] == 'G' and list1[1][i] == 'A':
			transition += 1
		if list1[0][i] == 'G' and list1[1][i] == 'C':
			transversions += 1
	return float(transition/transversions)
# print ratio("rosalind_tran.txt")