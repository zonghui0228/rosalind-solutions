# ^_^ coding:utf-8 ^_^

"""
Comparing Spectra with the Spectral Convolution
url: http://rosalind.info/problems/conv/

Given: Two multisets of positive real numbers S1 and S2. The size of each multiset is at most 200.
Return: The largest multiplicity of S1⊖S2, as well as the absolute value of the number x maximizing (S1⊖S2)(x) (you may return any such value if multiple solutions exist).
"""

with open("../data/rosalind_conv.txt", "r") as f:
    s1 = [float(x) for x in f.readline().strip().split(" ")]
    s2 = [float(x) for x in f.readline().strip().split(" ")]
spectral_convolution = [round(i-j, 5) for i in s1 for j in s2]
spectral_convolution_count = {s:spectral_convolution.count(s) for s in spectral_convolution}
spectral_convolution_count_sorted = sorted(spectral_convolution_count.items(), key=lambda item:item[1], reverse=True)
print(spectral_convolution_count_sorted[0])
