# ^_^ coding:utf-8 ^_^

"""
Construct the De Bruijn Graph of a String
url: http://rosalind.info/problems/ba3d/

Given: An integer k and a string Text.
Return:DeBruijnk(Text), in the form of an adjacency list.
"""

def DeBruijn(text, k):
    result = {}
    for i in range(len(text)-k+1):
        if text[i:i+k-1] not in result.keys():
            result[text[i:i+k-1]] = text[i+1:i+k]
        else:
            result[text[i:i+k-1]] += ',' + text[i+1:i+k]
    return result

if __name__ == '__main__':
    with open('../data/rosalind_ba3d.txt', 'r') as f:
        k = int(f.readline().strip())
        text = f.readline().strip()
    r = DeBruijn(text, k)
    for key in sorted(r.keys()):
        print(key + ' -> ' + r[key])