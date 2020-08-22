# ^_^ coding: utf-8 ^_^

"""
Read Quality Distribution
url: http://rosalind.info/problems/phre/

Given: A quality threshold, along with FASTQ entries for multiple reads.
Return: The number of reads whose average quality is below the threshold.
"""

from Bio import SeqIO

def phre(data):
    count = 0
    with open(data, "r") as f:
        threshold = int(f.readline())
        for record in SeqIO.parse(f, "fastq"):
            quality = record.letter_annotations["phred_quality"]
            average_quality = sum(quality)/len(quality)
            if average_quality < threshold:
                count += 1
    print(count)
    return count

if __name__ == "__main__":
    data = "../data/rosalind_phre.txt"
    phre(data)
