# Open Reading Frames

# Sample Dataset
# >Rosalind_99
# AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

# Sample Output
# MLLGSFRLIPKETLIQVAGSSPCNLS
# M
# MGMTPRLGLESLLE
# MTPRLGLESLLE
def read_fasta(file):
	seq = {}
	fp = open(file, 'r')
	for line in fp:
		if line.startswith('>'):
			name = line.replace('>', '')
			name = name.replace('\n', '')
			seq[name] = ''
		else:
			seq[name] += line.replace('\n', '')
	fp.close()
	return seq
# print read_fasta("rosalind_orf.txt")

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

# print coding('GGG')
def switch(s):
	# str(s)
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
# print switch('TATCG')
# other seq

def result(sequence):
	s1 = ''
	s2 = ''
	s3 = ''
	result_list = []
	for i in range(0, len(sequence)-2, 3):
		s1 = s1 + str(coding(sequence[i:i+3]))
	# print s1
	for i in range(len(s1)):
		if s1[i] == 'M' and s1.find('~',i) != -1:
			result_list.append(s1[i:s1.find('~',i)])

	for i in range(1, len(sequence)-2, 3):
		s2 = s2 + str(coding(sequence[i:i+3]))
	# print s2
	for i in range(len(s2)):
		if s2[i] == 'M' and s2.find('~',i) != -1:
			result_list.append(s2[i:s2.find('~',i)])

	for i in range(2, len(sequence)-2, 3):
		s3 = s3 + str(coding(sequence[i:i+3]))
	# print s3
	for i in range(len(s3)):
		if s3[i] == 'M' and s3.find('~',i) != -1:
			result_list.append(s3[i:s3.find('~',i)])
	return result_list

def main(file):
	seq = read_fasta(file)
	sequence = ''
	for i in seq.keys():
		sequence = seq[i]
	# print len(sequence)
	other_sequence = switch(sequence)
	# print other_sequence
	list1 = result(sequence)
	list2 = result(other_sequence)
	listall = list1 + list2
	list3 = []
	# print listall
	listall = list(set(listall))
	# print listall
	for i in listall:
		print i
# main("rosalind_orf.txt")
