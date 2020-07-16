# generate the k-mer composition of a string.

def composition(string, k):
	result = []
	for i in range(len(string) - k + 1):
		result.append(string[i:i+k])
	return result


if __name__ == '__main__':
	# f = open('test.txt', 'r')
	# k = int(f.readline().strip())
	# s = f.readline().strip()
	# f.close()
	s = 'TATGGGGTGC'
	k = 3
	for i in composition(s, k):
		print i