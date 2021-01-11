# ^_^ coding:utf-8 ^_^

"""
Find the distance between a pattern and a set of strings.
url: http://rosalind.info/problems/ba2h/

Given: A DNA string Pattern and a collection of DNA strings Dna.
Return: DistanceBetweenPatternAndStrings(Pattern, Dna).
"""

def calculateHammingDistance(a, b):
    hd = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            hd += 1
    return hd


def DistanceBetweenPatternAndStrings(pattern, strings):
    distance = 0
    k = len(pattern)
    for string in strings:
        hammingDistance = float("inf")
        for i in range(len(string)-k+1):
            k_pattern = string[i:i+k]
            hd = calculateHammingDistance(pattern, k_pattern)
            if hammingDistance > hd:
                hammingDistance = hd
        distance += hammingDistance
    return distance

if __name__ == "__main__":
    with open("../data/rosalind_ba2h.txt", "r") as f:
        pattern = f.readline().strip()
        strings = f.readline().strip().split(" ")
        distance = DistanceBetweenPatternAndStrings(pattern, strings)
        print(distance)
