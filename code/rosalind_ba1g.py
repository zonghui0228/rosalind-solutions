# ^_^ coding:utf-8 ^_^

"""
Compute the Hamming Distance Between Two Strings
url: http://rosalind.info/problems/ba1g/

Given: Two DNA strings.
Return: An integer value representing the Hamming distance.
"""

def HammingDistance(s1, s2):
	d = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			d += 1
	return d

if __name__ == "__main__":
    with open("../data/rosalind_ba1g.txt", "r") as f:
        s1 = f.readline().strip()
        s2 = f.readline().strip()
    d = HammingDistance(s1, s2)
    print(d)