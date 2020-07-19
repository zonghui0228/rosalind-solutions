# ^_^ coding:utf-8 ^_^

# Catalan Numbers and RNA Secondary Structures

from Bio import SeqIO

def _get_catalan_numbers(s, nodes, catalan_memo):
	n = int(nodes/2)
	if n <= 1:
		return 1
	if catalan_memo.get((s, nodes),0):
		return catalan_memo[(s, nodes)]
	Cn = 0
	for k in range(1, 2*n, 2):
		a, u, c, g = s[1:k].count("A"), s[1:k].count("U"), s[1:k].count("C"), s[1:k].count("G")
		if a==u and c==g and (s[0], s[k]) in [("A", "U"), ("U", "A"), ("C", "G"), ("G", "C")]:
			Cn += _get_catalan_numbers(s[1:k], k-1, catalan_memo) * _get_catalan_numbers(s[k+1:], 2*n-k-1, catalan_memo)
	# 记忆已经计算过的catalan数，减少计算复杂度
	catalan_memo[(s, nodes)] = Cn
	return Cn


if __name__ == "__main__":
	# load data
	seq_name, seq_string = [], []
	with open ("../data/rosalind_cat.txt",'r') as fa:
	    for seq_record  in SeqIO.parse(fa,'fasta'):
	        seq_name.append(str(seq_record.name))
	        seq_string.append(str(seq_record.seq))

	s = seq_string[0]
	print(s)
	nodes = len(s)
	catalan_memo = {} 	# 记忆已经计算过的catalan数，减少计算复杂度
	catalan_number= _get_catalan_numbers(s, nodes, catalan_memo)
	print("catalan number: {}".format(catalan_number))
	print("modulo 1,000,000: {}".format(catalan_number%1000000))
	