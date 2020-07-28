# ^_^ coding:utf-8 ^_^

"""
Computing GC Content
url: http://rosalind.info/problems/gc/

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""

from Bio import SeqIO

def gc(strings):
    gc_contents = {}
    for k, v in strings.items():
        gc_content = (v.count("G") + v.count("C")) / len(v)
        gc_contents[k] = gc_content
    gc_contents = sorted(gc_contents.items(), key=lambda d: d[1], reverse = True)
    highest_gc = gc_contents[0]
    return highest_gc

if __name__ == "__main__":
    # load data
    seq_name, seq_string = [], []
    with open ("../data/rosalind_gc.txt",'r') as fa:
        for seq_record  in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))
    strings = {seq_name[i]:seq_string[i] for i in range(len(seq_name))}
    highest_gc = gc(strings)
    print(highest_gc[0])
    print(highest_gc[1]*100)

# 	Rosalind_0483
# 52.74725274725275