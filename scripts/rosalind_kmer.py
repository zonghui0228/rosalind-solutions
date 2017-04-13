import itertools
fp = open('rosalind_kmer.txt', 'r')
string = ''
for line in fp:
	if line.startswith('>'):
		name = line.strip('\n').strip('>')
	else:
		string += line.strip('\n')
# print name, string

kmers = list("".join(x) for x in (itertools.product('ACGT', repeat = 4)))
seq = {}
for i in kmers:
	seq[i] = 0
for i in range(len(string) - 4 + 1):
	seq[string[i:i+4]] += 1
for i in kmers:
	print seq[i],