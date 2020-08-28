# ^_^ coding:utf-8 ^_^

"""
Construct the De Bruijn Graph of a Collection of k-mers
url: http://rosalind.info/problems/ba3e/

Given: A collection of k-mers Patterns.
Return: The de Bruijn graph DeBruijn(Patterns), in the form of an adjacency list.
"""

def debruijn(patterns):
    result = {}
    for i in patterns:
        if i[:-1] not in result.keys():
            result[i[:-1]] = i[1:]
        else:
            result[i[:-1]] += ','+ i[1:]
    return result

if __name__ == '__main__':
    with open('../data/rosalind_ba3e.txt', 'r') as f:
        p = [line.strip() for line in f.readlines()]
    res = debruijn(p)
    for i in sorted(res.keys()):
        print(i+' -> '+res[i])