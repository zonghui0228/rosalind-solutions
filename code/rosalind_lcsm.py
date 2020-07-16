# coding:utf-8
# Finding a Shared Motif

def read_fasta(file):
	fp = open(file, 'r')
	seq = {}
	for line in fp:
		if line.startswith('>'):
			name = line.replace('>', '')
			name = name.replace('\n', '')
			seq[name] = ''
		else:
			seq[name] += line.replace('\n', '')
	fp.close()
	return seq
	
def shortest_seq(seq):					
	min_len = 10000
	shortest_seq = ''
	for i in seq.keys():
		if len(seq[i]) < min_len:
			min_len = len(seq[i])
			shortest_seq = seq[i]
	return shortest_seq

def shared_motif(file):
	seq = read_fasta(file)
	# print seq
	s_seq = shortest_seq(seq)
	# print s_seq
	motif = set()
	for i in range(len(s_seq)):
		for j in range(i+1,len(s_seq)+1):
			motif.add(s_seq[i:j])
	for s in seq.values():
		update_motif = list(motif)
		for m in update_motif:
			if m not in s:
				motif.remove(m)
	# print motif
	n = 0
	longest_motif = ''
	for i in motif:
		if len(i) > n:
			longest_motif = i
			n = len(i)
	return longest_motif


if __name__ == "__main__":
	# s = read_fasta("test.txt")
	# print shortest_seq(s)
	print shared_motif("test.txt")
