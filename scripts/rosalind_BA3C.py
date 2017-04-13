# construct the overlap graph of a collection of k-mers.
def overlap(patterns):
	n = len(patterns)
	# m = 0
	if n < 2:
		print "the length of patterns must more than 2."
	else:
		for i in range(n):
			for j in range(n):
				if i != j and patterns[i][1:] == patterns[j][:-1]:
					print patterns[i], '->', patterns[j]
					# m += 1
	# print n, m
	# m add 1 should equal to n
if __name__ == '__main__':
	f = open('test.txt', 'r')
	patterns = []
	for line in f.readlines():
		patterns.append(line.strip())
	overlap(patterns)
	f.close()
	# print patterns