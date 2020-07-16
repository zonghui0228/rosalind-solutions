# Implement the Viterbi Algorithm
def patterncount(text, pattern):
	count = 0
	for i in range(len(text)-len(pattern)+1):
		# print text[i:i+len(pattern)]
		if text[i:i+len(pattern)] == pattern:
			count = count + 1
	return count

# a = 'GCGCG'
# b = 'GCG'
# print patterncount(a, b)