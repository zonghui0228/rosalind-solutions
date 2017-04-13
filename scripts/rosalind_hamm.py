# coding:utf-8
# Counting Point Mutations

# Sample Dataset
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT

# Sample Output
#7

def hamming_distance(file):
	fp = open(file, 'r')
	seq_list = []
	distances = 0
	for line in fp:
		seq_list.append(line.replace('\n', ''))
	for i in range(len(seq_list[0])):
		if seq_list[0][i] != seq_list[1][i]:
			distances += 1
	print distances

# hamming_distance("rosalind_hamm.txt")
