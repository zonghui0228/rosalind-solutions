# ^_^ coding:utf-8 ^_^

"""
Compute the Probability of an Outcome Given a Hidden Path
url: http://rosalind.info/problems/ba10b/

Given: A string x, followed by the alphabet Σ from which x was constructed, followed by a hidden path π, followed by the states States and emission matrix Emission of an HMM (Σ, States, Transition, Emission).
Return: The conditional probability Pr(x|π) that string x will be emitted by the HMM given the hidden path π.
"""

import numpy as np
import pandas as pd

def ConditionalProbability(π, x, Emission):
    prob = 1
    for i in range(len(π)):
        prob *= Emission.loc[π[i], x[i]]
    return prob

if __name__ == "__main__":
    with open("../data/rosalind_ba10b.txt", "r") as f:
        x = f.readline().strip()
        f.readline() # --------
        Σ = f.readline().strip().split()
        f.readline() # --------
        π = f.readline().strip()
        f.readline() # --------
        States = f.readline().strip().split()
        f.readline() # --------
        Emission = pd.DataFrame(np.full((len(States), len(Σ)), 0), index=States, columns=Σ)
        f.readline() # --------

        for line in f:
            l = line.strip().split()
            for i in range(1, len(l)):
                Emission.loc[l[0], Σ[i-1]] = float(l[i])
    # print(x, Σ)
    # print(π, States)
    # print(Emission)
    p = ConditionalProbability(π, x, Emission)
    print(p)
