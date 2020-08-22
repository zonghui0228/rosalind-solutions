# ^_^ coding:utf-8 ^_^

"""
Read Filtration by Quality
url: http://rosalind.info/problems/filt/

Given: A quality threshold value q, percentage of bases p, and set of FASTQ entries.
Return: Number of reads in filtered FASTQ entries
"""

from Bio import SeqIO

def quality_filtration(data):
    count = 0
    with open(data, "r") as f:
        t, p = map(int, f.readline().strip().split())
        for record in SeqIO.parse(f,"fastq"):
            phred=record.letter_annotations["phred_quality"]
            passes = 0
            for ph in phred:
                if ph >= t:
                    passes += 1
            if (passes/len(phred))*100 >= p:
                count += 1
    return count

if __name__ == "__main__":
    data = "../data/rosalind_filt.txt"
    count = quality_filtration(data)
    print(count)
