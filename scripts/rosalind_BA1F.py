# Find a Position in a Genome Minimizing the Skew

def minimum_skew(s):
	count_G = 0
	count_C = 0
	list_skew = [0]
	for i in range(len(s)):
		if s[i] == 'G':
			count_G += 1
		elif s[i] == 'C':
			count_C += 1
		list_skew.append(count_G - count_C)
	# print list_skew
	min_skew = min(list_skew)
	for i in range(len(list_skew)):
		if list_skew[i] == min_skew:
			print i,
def main(file):
	import linecache
	string = linecache.getline(file, 1).strip('\n')
# print string
	minimum_skew(string)
# main("rosalind_ba1f.txt")