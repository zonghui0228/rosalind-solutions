# !python3


# Problem
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string  is the string  formed by reversing the symbols of , then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string  of length at most 1000 bp.
# Return: The reverse complement  of .

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
