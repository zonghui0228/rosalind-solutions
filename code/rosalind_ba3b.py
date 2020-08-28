# ^_^ coding:utf-8 ^_^

"""
Reconstruct a String from its Genome Path
url: http://rosalind.info/problems/ba3b/

Given: A sequence of k-mers Pattern1, ... , Patternn such that the last k - 1 symbols of Patterni are equal to the first k - 1 symbols of Patterni+1 for i from 1 to n-1.
Return: A string Text of length k+n-1 where the i-th k-mer in Text is equal to Patterni for all i.
"""

def genome(sequences):
    string = sequences[0]
    for i in range(1, len(sequences)):
        string += sequences[i][-1]
    return string

if __name__ == '__main__':
    with open('../data/rosalind_ba3b.txt', 'r') as f:
        s = [line.strip() for line in f.readlines()]
    print(genome(s))