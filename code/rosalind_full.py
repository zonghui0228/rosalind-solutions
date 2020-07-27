# ^_^ coding:utf-8 ^_^

"""
Inferring Peptide from Full Spectrum
url: http://rosalind.info/problems/full/

Given: A list L containing 2n+3 positive real numbers (n≤100). The first number in L is the parent mass of a peptide P, and all other numbers represent the masses of some b-ions and y-ions of P (in no particular order). You may assume that if the mass of a b-ion is present, then so is that of its complementary y-ion, and vice-versa.
Return: A protein string t of length n for which there exist two positive real numbers w1 and w2 such that for every prefix p and suffix s of t, each of w(p)+w1 and w(s)+w2 is equal to an element of L. (In other words, there exists a protein string whose t-prefix and t-suffix weights correspond to the non-parent mass values of L.) If multiple solutions exist, you may output any one.
"""

import random

monoisotopic_mass_table = {
"A": 71.03711,
"C": 103.00919,
"D": 115.02694,
"E": 129.04259,
"F": 147.06841,
"G": 57.02146,
"H": 137.05891,
"I": 113.08406,
"K": 128.09496,
"L": 113.08406,
"M": 131.04049,
"N": 114.04293,
"P": 97.05276,
"Q": 128.05858,
"R": 156.10111,
"S": 87.03203,
"T": 101.04768,
"V": 99.06841,
"W": 186.07931,
"Y": 163.06333, 
}
monoisotopic_mass_table_ = {v:k for k,v in monoisotopic_mass_table.items()}

def inferring_peptide(L, monoisotopic_mass_table):
    t = []
    n = (len(L) - 3) // 2
    parent_mass=L[0]
    BYions = sorted(L[1:], key=lambda x: x)
    print(BYions)
    for i in range(n):
        print(BYions[2*i+1] - BYions[2*i], BYions[2*i+3] - BYions[2*i+2])

    # for i in range((n+1)//2):
    #     print(BYions[n+2*i+2]-BYions[n-2*i], BYions[n+2*i+1]-BYions[n-2*i-1])
    #     # assert round(BYions[n+2*i+2]-BYions[n-2*i], 5) == round(BYions[n+2*i+1]-BYions[n-2*i-1], 5)
    #     if i==0:
    #         pass
    #         # print(n-2*i-1, n-2*i, n+2*i+1, n+2*i+2)
    #         # print(round(BYions[n-2*i] - BYions[n-2*i-1], 5), round(BYions[n+2*i+2] - BYions[n+2*i+1], 5))
    #         # s = monoisotopic_mass_table_.get(round(BYions[n+2*i+2]-BYions[n-2*i], 5), 1)
    #         # t = [s]
    #     else:
    #         pass
            # print(n-2*i-1, n-2*i, n+2*i+1, n+2*i+2)
            # print(round(BYions[n-2*i] - BYions[n-2*i-1], 5), round(BYions[n+2*i+2] - BYions[n+2*i+1], 5))
            # value1 = round(BYions[n-2*i] - BYions[n-2*i-1], 5)
            # value2 = round(BYions[n+2*i+2] - BYions[n+2*i+1], 5)
            # print(value1, value2)

        # print(L[i+8]-L[i+7])
    return t

if __name__ == "__main__":
    # load data
    with open("../data/rosalind_full.txt", "r") as f:
        L = [float(line.strip()) for line in f]
    string = inferring_peptide(L, monoisotopic_mass_table)
    print(string)
# t = "KEKEP"
print(128.09496 + 129.04259 + 128.09496 + 129.04259 + 97.05276)
print(766.492149105-610.391039105, 863.544909105-738.485999105)
print(766.492149105-738.485999105, 863.544909105-610.391039105)
print(1377.8200091+610.391039105)
print(1377.8200091-738.485999105)
print(1249.7250491-610.391039105)

