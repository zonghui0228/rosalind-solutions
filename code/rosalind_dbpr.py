# ^_^ coding:utf-8 ^_^

"""
Introduction to Protein Databases
url: http://rosalind.info/problems/dbpr/

Given: The UniProt ID of a protein.
Return: A list of biological processes in which the protein is involved (biological processes are found in a subsection of the protein's "Gene Ontology" (GO) section).
"""

import re
from Bio import ExPASy

def dbpr(UniProt_ID):
    handle = ExPASy.get_sprot_raw(UniProt_ID)
    record = handle.read()
    bp_patten = r"P:.*; IEA:"
    bp_res = re.findall(bp_patten, str(record))
    bp = [r.replace("P:", "").replace("; IEA:", "") for r in bp_res]
    handle.close()
    return bp

if __name__ == "__main__":
    with open("../data/rosalind_dbpr.txt", "r") as f:
        UniProt_ID = f.readline().strip()
    bp = dbpr(UniProt_ID)
    print("\n".join(bp))
    