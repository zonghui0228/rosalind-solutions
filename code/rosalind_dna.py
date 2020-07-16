# !python3
# Given: A DNA string  of length at most 1000 nt
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in

def count_DNA(string):
	countA, countC, countG, countT=0, 0, 0, 0
	i=0
	while i < len(string):
		if string[i] == 'A':
			countA = countA + 1
		elif string[i] == 'C':
			countC = countC + 1
		elif string[i] == 'G':
			countG = countG + 1
		elif string[i] == 'T':
			countT = countT+1
		i = i+1
	return countA, countC, countG, countT


if __name__ == "__main__":
	with open("../data/rosalind_dna.txt", 'r') as f:
		string = f.readline().strip()
		countA, countC, countG, countT = count_DNA(string)
		print(countA, countC, countG, countT)



