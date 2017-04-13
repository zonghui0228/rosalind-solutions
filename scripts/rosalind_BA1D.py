# Find All Occurrences of a Pattern in a String
def positions_pattern(pattern, string):
	for i in range(len(string)-len(pattern)+1):
		if string[i:i+len(pattern)] == pattern:
			print i,

p = 'ATAT'
s = 'GATATATGCATATACTT'
positions_pattern(p, s)