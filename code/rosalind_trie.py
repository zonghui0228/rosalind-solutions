# Introduction to Pattern Matching.
def read_file(file):
	f = open(file, 'r')
	res = [line.strip('\n') for line in f]
	f.close()
	return res

def pattern_match(strings):
	for i in strings:
		for j in i:
			print j

if __name__ == "__main__":
	r = read_file("test.txt")
	# print r
	pattern_match(r) 