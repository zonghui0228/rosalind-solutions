# Compute the Probability of an Outcome Given a Hidden Path
s = 'yyzyzzzxyyzxyzyzzxxyzxxyzzzxzyzyxxyzzxzxxxzyzzyxxz'
t = 'ABBBBBBBABABBBBBBBAABABABBABABAABBAABBBBBBBAABABBA'
Ax = 0.277
Ay = 0.561
Az = 0.162
Bx = 0.425
By = 0.536
Bz = 0.039
prob = 1
for i in range(len(s)):
	if t[i] == 'A' and s[i] == 'x':
		prob = prob * Ax
	if t[i] == 'A' and s[i] == 'y':
		prob = prob * Ay 
	if t[i] == 'A' and s[i] == 'z':
		prob = prob * Az
	if t[i] == 'B' and s[i] == 'x':
		prob = prob * Bx
	if t[i] == 'B' and s[i] == 'y':
		prob = prob * By
	if t[i] == 'B' and s[i] == 'z':
		prob = prob * Bz
print prob