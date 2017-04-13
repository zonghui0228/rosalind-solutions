# construct the de Bruijn graph from a collection of k-mers.
def debruijn(patterns):
	result = {}
	for i in patterns:
		if i[:-1] not in result.keys():
			result[i[:-1]] = i[1:]
		else:
			result[i[:-1]] += ','+ i[1:]
	return result

if __name__ == '__main__':
	f = open('test.txt', 'r')
	p = [line.strip() for line in f.readlines()]
	r = debruijn(p)
	# print r
	for i in sorted(r.keys()):
		print i, '->', r[i]
	f.close()