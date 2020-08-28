# ^_^ coding:utf-8 ^_^

"""
Implement PatternToNumber
url: http://rosalind.info/problems/ba1l/

Given: A DNA string Pattern.
Return: PatternToNumber(Pattern).
"""

def PatternToNumber(pattern):
    seq = {'A':0, 'C':1, 'G':2, 'T':3}
    k = len(pattern)
    num = 0
    for i in range(k):
        num += seq[pattern[i]] * pow(4, k-i-1)
    return num

if __name__ == "__main__": 
    # pattern = 'AGT'
    with open("../data/rosalind_ba1l.txt", "r") as f:
        pattern = f.readline().strip()
    print(PatternToNumber(pattern))