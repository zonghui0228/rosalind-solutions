# Find the Most Frequent Words in a String
s = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
list1 = []
for i in range(len(s)-k+1):
	list1.append(s[i:i+k])
maxmium = 0
for i in list1:
	if list1.count(i) > maxmium:
		maxmium = list1.count(i)
list2 = list(set(list1))
for i in list2:
	if list1.count(i) == maxmium:
		print i
	