# ^_^ coding:utf-8 ^_^

"""
The Wright-Fisher Model of Genetic Drift
url: http://rosalind.info/problems/wfmd/

Given: Positive integers N (N≤7), m (m≤2N), g (g≤6) and k (k≤2N).
Return: The probability that in a population of N diploid individuals initially possessing m copies of a dominant allele, we will observe after g generations at least k copies of a recessive allele. Assume the Wright-Fisher model.
"""

from scipy.special import comb

def WrightFisher_GeneticDrift(N, m, g, k):
    """
    Args:
        N: N diploid individuals
        m: initially possessing m copies of a dominant allele
        g: g generations
        k: at least k copies of a recessive allele
    Returns:
        probability
    """
    p = m/(2*N) # dominant allele
    q = 1 - p # recessive_allele

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
    
    print("answer: ", sum(prob[k-1:]))
    return prob

if __name__ == "__main__":
    with open("../data/rosalind_wfmd.txt", "r") as f:
        N, m, g, k = map(int, f.readline().strip().split())
    WrightFisher_GeneticDrift(N, m, g, k)
    # N=4, m=6, g=2, k=1, P=0.772
