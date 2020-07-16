# Expected Number of Restriction Sites
n = 996264 
s = 'CTAGCTGT'
list1 = [0.000, 0.086, 0.111, 0.206, 0.249, 0.313, 0.372, 0.423, 0.475, 0.554, 0.592, 0.617, 0.710, 0.726, 0.796, 0.865, 0.896, 1.000]
at = s.count('A') + s.count('T')
gc = s.count('G') + s.count('C')
for i in list1:
	print pow((1-i)/2, at) * pow(i/2, gc) * (n-len(s)+1),
