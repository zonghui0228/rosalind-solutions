# construct the de Bruijn graph of a string.
def DeBruijn(text, k):
	result = {}
	for i in range(len(text)-k+1):
		if text[i:i+k-1] not in result.keys():
			result[text[i:i+k-1]] = text[i+1:i+k]
		else:
			result[text[i:i+k-1]] += ',' + text[i+1:i+k]
	return result


if __name__ == '__main__':
	f = open('test.txt', 'r')
	k = int(f.readline())
	t = f.readline().strip()
	r = DeBruijn(t, k)
	for key in sorted(r.keys()):
		print key, '->', r[key]
	f.close()