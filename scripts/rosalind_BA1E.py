# Find Patterns Forming Clumps in a String
def clump_finding(string, K, L, t):
	list1 = []
	for i in range(len(string)-L+1):
		for j in range(i,i+L-K):
			if string[i:i+L].count(string[j:j+K]) == t:
				list1.append(string[j:j+K])
	list2 = list(set(list1))
	for i in list2:
		print i,

s = 'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'
K = 5
L = 75
t = 4
clump_finding(s, K, L, t)