# ^_^ coding: utf-8 ^_^

"""
Protein Translation
url: http://rosalind.info/problems/ptra/

Given: A DNA string s of length at most 10 kbp, and a protein string translated by s.
Return: The index of the genetic code variant that was used for translation. (If multiple solutions exist, you may return any one.)
"""

import random
from Bio.Seq import translate

def genetic_code(dna, protein):
    res = []
    table_ids = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]
    for t in table_ids:
        if translate(dna, table=t, to_stop=True) == protein:
            res.append(t)
    return res

if __name__ == "__main__":
    with open("../data/rosalind_ptra.txt", "r") as f:
        dna = f.readline().strip()
        protein = f.readline().strip()
    res = genetic_code(dna, protein)
    print(random.choice(res))