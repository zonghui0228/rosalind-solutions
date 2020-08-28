# ^_^ coding:utf-8 ^_^

"""
Compute the Probability of a Hidden Path
url: http://rosalind.info/problems/ba10a/

Given: A hidden path π followed by the states States and transition matrix Transition of an HMM (Σ, States, Transition, Emission).
Return: The probability of this path, Pr(π). You may assume that initial probabilities are equal.
"""

import numpy as np
import pandas as pd

def PathProbability(π, Transition):
    prob = 0.5
    for i in range(len(π)-1):
        prob *= Transition.loc[π[i], π[i+1]]
    return prob

if __name__ == "__main__":
    with open("../data/rosalind_ba10a.txt", "r") as f:
        π = f.readline().strip()
        f.readline() # --------
        States = f.readline().strip().split()
        Transition = pd.DataFrame(np.full((len(States), len(States)), 0), index=States, columns=States)
        f.readline() # --------
        States_col = f.readline().strip().split()

        for line in f:
            l = line.strip().split()
            for i in range(1, len(l)):
                Transition.loc[l[0], States_col[i-1]] = float(l[i])
    # print(π, States)
    # print(Transition)
    p = PathProbability(π, Transition)
    print(p)