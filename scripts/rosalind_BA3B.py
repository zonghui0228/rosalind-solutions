# find the string spelled by a genome path.
def genome(sequences):
	if len(sequences) == 0:
		print "the length of sequences can't be 0."
	elif len(sequences) == 1:
		return sequences[0]
	else:
		string = sequences[0]
		for i in range(1, len(sequences)):
			string += sequences[i][-1]
		return string

if __name__ == '__main__':
	f = open('test.txt', 'r')
	s = []
	for line in f.readlines():
		s.append(line.strip())
	print genome(s)
	f.close()