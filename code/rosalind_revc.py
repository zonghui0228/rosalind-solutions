# ^_^ coding:utf-8 ^_^

""""
Complementing a Strand of DNA
url: http://rosalind.info/problems/revc/

# Given: A DNA string  of length at most 1000 bp.
# Return: The reverse complement sc of s. .
"""

def DNAstrand(string):
    strand = ""
    for i in string[::-1]:
        if i == "A":
            strand += "T"
        if i == "T":
            strand += "A"
        if i == "C":
            strand += "G"
        if i == "G":
            strand += "C"
    return strand


if __name__ == "__main__":
    with open("../data/rosalind_revc.txt", "r") as f:
        string = f.readline().strip()
        strand = DNAstrand(string)
        print(strand)
