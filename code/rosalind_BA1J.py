# Given: A DNA string Text as well as integers k and d.
# Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, reverse Pattern) over all possible k-mers.
def neighbour(pattern, mismatch, words):
	if mismatch == 0:
		words.add(pattern)
	else:
		bases = ['A', 'T', 'C', 'G']
		for i in range(len(pattern)):
			for j in range(len(bases)):
			# if mismatch == 0:
			# 	words.add(pattern)
				new_pattern = pattern[:i] + bases[j] + pattern[i+1:]
				if mismatch <= 1:
					words.add(new_pattern)
				else:
					neighbour(new_pattern, mismatch - 1, words)

def ReversePattern(pattern):
	reversepattern = ''
	for i in range(len(pattern), 0, -1):
		if pattern[i - 1] == 'A':
			reversepattern += 'T'
		elif pattern[i - 1] == 'T':
			reversepattern += 'A'
		elif pattern[i - 1] == 'G':
			reversepattern += 'C'
		elif pattern[i - 1] == 'C':
			reversepattern += 'G'
	return reversepattern
# print ReversePattern('ATGC')

def FindMostFrequentPattern(text, k, d):
	allfrequentwords = defaultdict(int)
	for i in range(len(text) - k + 1):
		frequentwords = set()
		# reversefrequentwords = set()
		neighbour(text[i:i + k], d, frequentwords)
		# for i in frequentwords:
		# 	reversefrequentwords.add(reversepattern(i))
		for words in frequentwords:
			allfrequentwords[words] += 1
	# print allfrequentwords
	for t in allfrequentwords.keys():
		reverse_k = ReversePattern(t)
		for i in range(len(text) - k + 1):
			if hamming_distance(text[i:i + k], reverse_k) <= d:
				allfrequentwords[t] += 1
	# print allfrequentwords
	result = set()
	for t in allfrequentwords.keys():
		if allfrequentwords[t] == max(allfrequentwords.values()):
			result.add(t)
			result.add(ReversePattern(t))
	for i in result:
		print i,
		
# from collections import defaultdict
# from rosalind_BA1H import hamming_distance
# text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
# k = 4
# d = 1
# FindMostFrequentPattern(text, k, d)







