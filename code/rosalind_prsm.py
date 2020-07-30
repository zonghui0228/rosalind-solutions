# ^_^ coding:utf-8 ^_^

"""
Matching a Spectrum to a Protein
url: http://rosalind.info/problems/prsm/

Given: A positive integer n followed by a collection of n protein strings s1, s2, ..., sn and a multiset R of positive numbers (corresponding to the complete spectrum of some unknown protein string).
Return: The maximum multiplicity of R⊖S[sk] taken over all strings sk, followed by the string sk for which this maximum multiplicity occurs (you may output any such value if multiple solutions exist).
"""

monoisotopic_mass_table = {
    "A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259, "F": 147.06841,
    "G": 57.02146, "H": 137.05891, "I": 113.08406, "K": 128.09496, "L": 113.08406,
    "M": 131.04049, "N": 114.04293, "P": 97.05276, "Q": 128.05858, "R": 156.10111,
    "S": 87.03203, "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333, 
    }

def get_multiplicity(string, multiset):
    complete_spectrum = []
    for i in range(len(string)):
        prefix, suffix = string[:i], string[i:]
        prefix_weights = round(sum([monoisotopic_mass_table.get(i,0) for i in prefix]), 5)
        suffix_weights = round(sum([monoisotopic_mass_table.get(i,0) for i in suffix]), 5)
        complete_spectrum.append(prefix_weights)
        complete_spectrum.append(suffix_weights)

    spectral_convolution = [round(i-j, 5) for i in complete_spectrum for j in multiset]
    spectral_convolution_count = {s:spectral_convolution.count(s) for s in spectral_convolution}
    spectral_convolution_count_sorted = sorted(spectral_convolution_count.items(), key=lambda item:item[1], reverse=True)
    # print(spectral_convolution_count_sorted[0])
    return [string] + list(spectral_convolution_count_sorted[0])

if __name__ == "__main__":
    string = []
    multiset = []
    with open("../data/rosalind_prsm.txt", "r") as f:
        num_strings = int(f.readline().strip())
        for i in range(num_strings):
            string.append(f.readline().strip())
        for line in f:
            multiset.append(float(line.strip()))

    multiplicities = []
    for s in string:
        multiplicities.append(get_multiplicity(s, multiset))
    multiplicities_sorted = sorted(multiplicities, key=lambda x:x[2], reverse=True)
    print(multiplicities_sorted[0])