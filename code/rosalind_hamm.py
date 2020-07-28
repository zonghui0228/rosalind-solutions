# ^_^ coding:utf-8 ^_^

"""
Counting Point Mutations
url: http://rosalind.info/problems/hamm/

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
"""

def hamm(string1, string2):
    distance = 0
    assert len(string1) == len(string2)
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1
    return distance

if __name__ == "__main__":
    with open("../data/rosalind_hamm.txt", "r") as f:
        string1 = f.readline().strip()
        string2 = f.readline().strip()
    print(hamm(string1, string2))
