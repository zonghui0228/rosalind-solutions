# ^_^ coding:utf-8 ^_^

"""
Inferring Protein from Spectrum
url: http://rosalind.info/problems/spec/

Given: A list L of n (n≤100) positive real numbers.
Return: A protein string of length n−1 whose prefix spectrum is equal to L (if multiple solutions exist, you may output any one of them). Consult the monoisotopic mass table.
"""

import random

monoisotopic_mass_table= {
    "A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259, "F": 147.06841,
    "G": 57.02146, "H": 137.05891, "I": 113.08406, "K": 128.09496, "L": 113.08406,
    "M": 131.04049, "N": 114.04293, "P": 97.05276, "Q": 128.05858, "R": 156.10111,
    "S": 87.03203, "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333, 
}

def inferring_protein(L, monoisotopic_mass_table):
    string = [""]
    for i in range(len(L)-1):
        mass = L[i+1] - L[i]
        new_s = [k for k, v in monoisotopic_mass_table.items() if round(mass, 2) == round(v, 2)]
        string = [s+ns for s in string for ns in new_s]
    
    for s in string:
        assert len(s) == len(L)-1
    print(len(string))
    return string

if __name__ == "__main__":
    # load data
    with open("../data/rosalind_spec.txt", "r") as f:
        L = [float(line.strip()) for line in f]
    string = inferring_protein(L, monoisotopic_mass_table)
    print(random.sample(string, k=1))

