# ^_^ coding:utf-8 ^_^

"""
Implement NumberToPattern
url: http://rosalind.info/problems/ba1m/

Given: Integers index and k.
Return: NumberToPattern(index, k).
"""

def NumberToPattern(index, k):
    bases = ['A', 'C', 'G', 'T']
    pattern = ''
    for i in range(k):
        pattern += bases[index % 4]
        index = index // 4
    return pattern[::-1]

if __name__ == "__main__":
    with open("../data/rosalind_ba1m.txt", "r") as f:
        index = int(f.readline().strip())
        k = int(f.readline().strip())
    print(NumberToPattern(index, k))
