# ^_^ coding:utf-8 ^_^

"""
Locating Restriction Sites
url: http://rosalind.info/problems/revp/

Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
"""

from Bio import SeqIO

def switch(s):
    s = s[::-1]
    # print s
    switch_s = ''
    for i in range(len(s)):
        if s[i] == 'A':
            switch_s += 'T'
        elif s[i] == 'T':
            switch_s += 'A'
        elif s[i] == 'G':
            switch_s += 'C'
        elif s[i] == 'C':
            switch_s += 'G'
    return switch_s

def palindrome(s):
    for i in range(len(s)):
        for j in range(4,13,1):
            if s[i:i+j] == switch(s[i:i+j]) and (i+j <= len(s)):
                print(i+1, j)

if __name__ == "__main__":
    # load data
    seq_name, seq_string = [], []
    with open ("../data/rosalind_revp.txt",'r') as fa:
        for seq_record  in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))
    s = seq_string[0]
    palindrome(s)