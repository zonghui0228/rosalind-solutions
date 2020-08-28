# ^_^ coding:utf-8 ^_^

"""
Generate the k-mer Composition of a String
url: http://rosalind.info/problems/ba3a/

Given: An integer k and a string Text.
Return: Compositionk(Text) (the k-mers can be provided in any order).
"""

def composition(string, k):
    result = []
    for i in range(len(string) - k + 1):
        result.append(string[i:i+k])
    return result

if __name__ == '__main__':
    # s = 'CAATCCAAC'
    # k = 5
    with open("../data/rosalind_ba3a.txt", "r") as f:
        k = int(f.readline().strip())
        s = f.readline().strip()
    res = composition(s, k)
    print("\n".join(res))