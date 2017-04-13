# Matching Random Motifs 


N = 97698
x = 0.462550
s = 'AGATGGCCA'
at = s.count('A') + s.count('T')
gc = s.count('G') + s.count('C')
P_s = pow(x/2, gc) * pow((1-x)/2, at)
print 1 - pow(1 - P_s, N)
