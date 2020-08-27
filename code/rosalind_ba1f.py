# ^_^ coding:utf-8 ^_^

"""
Find a Position in a Genome Minimizing the Skew
url: http://rosalind.info/problems/ba1f/

Given: A DNA string Genome.
Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).
"""

def MinimumSkew(s):
	skew = [0]
	for i in range(len(s)):
		if s[i] == "G":
			skew.append(skew[-1]+1)
		elif s[i] == "C":
			skew.append(skew[-1]-1)
		else:
			skew.append(skew[-1])
	# print(skew)
	minimum_skew = min(skew)
	for i in range(len(skew)):
		if skew[i] == minimum_skew:
			print(i, end=" ")
	print()
	return skew

if __name__ == "__main__":
	# s = "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"
	
	with open("../data/rosalind_ba1f.txt", "r") as f:
		s = f.readline().strip()
	MinimumSkew(s)