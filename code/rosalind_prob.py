# Introduction to Random Strings

import math
s = 'CTCTGCAATGCGACCAGATCCGGGCTTCTTTCTATCCATCTAAGAACTAAGTAAACACATTACTCTACCGAGCAAGTGCT'
a = s.count('A') + s.count('T')
c = s.count('C') + s.count('G')
print a, c
list_GC = [0.058, 0.144, 0.210, 0.277, 0.318, 0.342, 0.406, 0.483, 0.549, 0.563, 0.666, 0.686, 0.777, 0.784, 0.845, 0.900]
for i in list_GC:
	print a * math.log((1-i)/2, 10) + c * math.log(i/2, 10),