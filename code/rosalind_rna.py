# !python3

# Given: A DNA string  having length at most 1000 nt.
# Return: The transcribed RNA string of .


def dna2rna(string):
    return string.replace('T','U')


if __name__ == "__main__":
    with open("../data/rosalind_rna.txt", 'r') as f:
        string = f.readline().strip()
        rst = dna2rna(string)
        print(rst)

