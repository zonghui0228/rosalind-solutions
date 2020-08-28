# ^_^ coding:utf-8 ^_^

"""
Implement GreedyMotifSearch
url: http://rosalind.info/problems/ba2d/

Given: Integers k and t, followed by a collection of strings Dna.
Return: A collection of strings BestMotifs resulting from running GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.
"""

def HammingDistance(a,b):
	count  = 0
	for i in range(len(a)):
		if a[i] != b[i]:
			count += 1
	return count

def ProfileMostProbableKmer(string, k, motif):
	dis = HammingDistance(string[0:k], motif)
	MostProbableKmer = string[0:k]
	for i in range(len(string) - k + 1):
		if HammingDistance(string[i:i+k], motif) < dis:
			MostProbableKmer = string[i:i+k]
			dis = HammingDistance(string[i:i+k], motif)
	return MostProbableKmer
# print ProfileMostProbableKmer("AAGAATCAGTCA", 3, "GGC")

def Score1(a, b):
	# a, b is a list
	score = 0
	for i in range(len(a)):
		sc = HammingDistance(a[i][0:len(b[i])], b[i])
		for j in range(len(a[i]) - len(b[i]) + 1):			
			if HammingDistance(a[i][j:j+len(b[i])], b[i]) <= sc:
				sc = HammingDistance(a[i][j:j+len(b[i])], b[i])
		score += sc
	return score
def Score2(a, b):
	# a is a string, b is a list
	score = 0
	for i in b:
		sc = HammingDistance(a[0:len(i)], i)
		for j in range(len(a) - len(i) + 1):
			if HammingDistance(a[j:j+len(i)],i) < sc:
				sc = HammingDistance(a[j:j+len(i)],i)
		score += sc
	return score

def Score3(s):
	# s is a sting
	score = 0
	for i in range(1,len(s)):
		score += HammingDistance(s[0],s[i])
	return score

def Score4(a,b):
	sc = HammingDistance(a[0:len(b)] , b)
	for i in range(len(a) - len(b) + 1):
		if HammingDistance(a[i:i+len(b)], b) < sc:
			sc = HammingDistance(a[i:i+len(b)], b)
	return sc
# print score('GGCGTTCAGGCA','GAC')

def GreedyMotifSearch(dna, k, t):
	from rosalind_BA2C import *
	bestMotifs = []
	for string in dna:
		bestMotifs.append(string[0:k]) 
	print bestMotifs
	matrix = [[0.25,0.25,0],[0,0.25,0],[0.5,0.25,0],[0.25,0.25,0]]
	for i in range(len(dna[0]) - k + 1):
		# print i
		motifs = []
		motifs.append(dna[0][i:i+k])
		# print motifs
		for j in range(1, len(dna)):
			motifs.append(FindProfileMostProbableKmer(dna[j], k, matrix))
		print motifs
		if Score1(dna, motifs) < Score1(dna, bestMotifs):
			bestMotifs = motifs
	# return bestMotifs


fp = open("rosalind_ba2d.txt")
file_list = []
for line in fp.readlines():
	file_list.append(line.strip())
k = int(file_list[1].split(' ')[0])
t = int(file_list[1].split(' ')[1])
dna = file_list[2:t + 2]
print GreedyMotifSearch(dna, k ,t)
fp.close()