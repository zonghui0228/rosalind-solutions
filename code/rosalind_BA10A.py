# Compute the Probability of a Hidden Path
s = 'BAAABABBBBBABABAAABBABABBBBABBAABAABBBABBAAAAABBBB'
aa = 0.144
ab = 0.856
ba = 0.596
bb = 0.404
score = 0.5
for i in range(len(s)-1):
	# print s[i:i+2]
	if s[i:i+2] == 'AA':
		score = score * aa 
	if s[i:i+2] == 'AB':
		score = score * ab 
	if s[i:i+2] == 'BA':
		score = score * ba 
	if s[i:i+2] == 'BB':
		score = score * bb 
print score