# ^_^ coding:utf-8 ^_^

"""
The Founder Effect and Genetic Drift
url: http://rosalind.info/problems/foun/

Given: Two positive integers N and m, followed by an array A containing k integers between 0 and 2N. A[j] represents the number of recessive alleles for the j-th factor in a population of N diploid individuals.
Return: An m×k matrix B for which Bi,j represents the common logarithm of the probability that after i generations, no copies of the recessive allele for the j-th factor will remain in the population. Apply the Wright-Fisher model.
"""

from scipy.special import comb
import numpy as np

def WrightFisher_GeneticDrift(N, m, g):
    q = m/(2*N) # dominant allele
    p = 1 - q # recessive_allele

    # the probability of exactly i copies of recessive allele in 1st generation.
    prob = [comb(2*N,i) * (q**(i)) * (p**(2*N-i)) for i in range(1, 2*N+1)]

    # the probability of exactly t copies of recessive allele in next generation.
    for gen in range(1, g):
        gen_prob = []

        # probability of exactly t copies of recessive allele in "gen" generation
        for t in range(1, 2*N+1):
            # this generation, copies (t) of recessive allele range from 1 to 2*N.
            # last generation, copies (i) of recessive allele range from 1 to 2*N,
            # for each possible copies t, we calculated probability from i to t.
            prob_t = [comb(2*N,t) * ((i/(2*N))**(t)) * ((1-(i/(2*N)))**(2*N-t)) for i in range(1, 2*N+1)]
            gen_prob.append(sum([prob_t[j] * prob[j] for j in range(2*N)]))
        prob = gen_prob

    # print(np.log10(1-sum(prob)))
    return np.log10(1-sum(prob))

def foun(N, m, A):
    k = len(A)
    B = np.zeros([m, k])
    for i in range(m):
        for j in range(k):
            B[i,j] = WrightFisher_GeneticDrift(N, A[j], i+1)
    return B

if __name__ == "__main__":
    with open("../data/rosalind_foun.txt", "r") as f:
        N, m = map(int, f.readline().strip().split())
        A = [int(i) for i in f.readline().strip().split()]
    B = foun(N, m, A)
    for b in B:
        for bb in b:
            print(bb, end=" ")
        print()
        