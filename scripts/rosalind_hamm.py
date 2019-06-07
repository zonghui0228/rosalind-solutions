# python3


# Given: Two DNA strings  and  of equal length (not exceeding 1 kbp).
# Return: The Hamming distance


def hamm(string1, string2):
	distance = 0
	if len(string1) == len(string2):
		for i in range(len(string1)):
			if string1[i] != string2[i]:
				distance += 1
	return distance


if __name__ == "__main__":
	with open("../data/rosalind_hamm.txt", "r") as f:
		string1 = f.readline().strip()
		string2 = f.readline().strip()
		print(hamm(string1, string2))


