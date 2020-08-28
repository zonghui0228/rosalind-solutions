# ^_^ coding:utf-8 ^_^

"""
Construct the Overlap Graph of a Collection of k-mers
url: http://rosalind.info/problems/ba3c/

Given: A collection Patterns of k-mers.
Return: The overlap graph Overlap(Patterns), in the form of an adjacency list.
"""

def overlap(patterns):
    n = len(patterns)
    for i in range(n):
        for j in range(n):
            if i != j and patterns[i][1:] == patterns[j][:-1]:
                print(patterns[i] + ' -> ' + patterns[j])

if __name__ == '__main__':
    with open('../data/rosalind_ba3c.txt', 'r') as f:
        patterns = [line.strip() for line in f]
    overlap(patterns)