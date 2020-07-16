# Calculating Protein Mass
def weight(s):
	w = 0
	for i in s:
		if i == 'A':
			w += 71.03711
		if i == 'C':
			w += 103.00919
		if i == 'D':
			w += 115.02694
		if i == 'E':
			w += 129.04259
		if i == 'F':
			w += 147.06841
		if i == 'G':
			w += 57.02146
		if i == 'H':
			w += 137.05891
		if i == 'I':
			w += 113.08406
		if i == 'K':
			w += 128.09496
		if i == 'L':
			w += 113.08406
		if i == 'M':
			w += 131.04049
		if i == 'N':
			w += 114.04293
		if i == 'P':
			w += 97.05276
		if i == 'Q':
			w += 128.05858
		if i == 'R':
			w += 156.10111
		if i == 'S':
			w += 87.03203
		if i == 'T':
			w += 101.04768
		if i == 'V':
			w += 99.06841
		if i == 'W':
			w += 186.07931
		if i == 'Y':
			w += 163.06333			
	return w

def main(file):
	fp = open(file, 'r')
	s = ''
	for line in fp:
		s += line
	return weight(s)

# print main("rosalind_prtm.txt")

