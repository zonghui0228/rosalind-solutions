# ^_^ coding:utf-8 ^_^

"""
Find All Approximate Occurrences of a Pattern in a String
url: http://rosalind.info/problems/ba1h/

Given: Strings Pattern and Text along with an integer d.
Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
"""

def HammingDistance(s1, s2):
    d = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            d += 1
    return d

def ApproximatePattern(pattern, text, d):
    positions = []
    for i in range(len(text)-len(pattern)+1):
        if HammingDistance(pattern, text[i:i+len(pattern)]) <= d:
            print(i, end=" ")
            positions.append(i)
    return positions

if __name__ == "__main__":
    with open("../data/rosalind_ba1h.txt", "r") as f:
        pattern = f.readline().strip()
        text = f.readline().strip()
        d = int(f.readline().strip())
    ApproximatePattern(pattern, text, d)