# ^_^ coding: utf-8 ^_^

"""
Base Quality Distribution
url: http://rosalind.info/problems/bphr/

Given: FASTQ file, quality threshold q
Return: Number of positions where mean base quality falls below given threshold
"""

from Bio import SeqIO

def bphr(data):
    count = 0
    with open(data, "r") as f:
        threshold = int(f.readline())
        qualities = []
        for record in SeqIO.parse(f, "fastq"):
            quality = record.letter_annotations["phred_quality"]
            qualities.append(quality)
    for i in range(len(qualities[0])):
        if sum([q[i] for q in qualities])/len(qualities) < threshold:
            count += 1
    return count

if __name__ == "__main__":
    data = "../data/rosalind_bphr.txt"
    count = bphr(data)
    print(count)
