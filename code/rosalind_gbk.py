# ^_^ coding:utf-8 ^_^

"""
GenBank Introduction
url: http://rosalind.info/problems/gbk/

Given: A genus name, followed by two dates in YYYY/M/D format.
Return: The number of Nucleotide GenBank entries for the given genus that were published between the dates specified.
"""

from Bio import Entrez
from bs4 import BeautifulSoup

def get_Nucleotide_GenBank_entries(genus_name, date1, date2):
    Entrez.email = "***@******"
    term = '"{}"[Organism] AND ("{}"[Publication Date] : "{}"[Publication Date])'.format(genus_name, date1, date2)
    handle = Entrez.esearch(db="nucleotide", term=term)
    records = handle.read()
    # print(records)
    soup = BeautifulSoup(records,'html.parser')
    handle.close()
    return soup.count.text


if __name__ == "__main__":
    with open("../data/rosalind_gbk.txt", "r") as f:
        genus_name = f.readline().strip()
        date1 = f.readline().strip()
        date2 = f.readline().strip()
    count = get_Nucleotide_GenBank_entries(genus_name, date1, date2)
    print(count)