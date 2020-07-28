# ^_^ coding:utf-8 ^_^

"""
Enumerating Gene Orders
url: http://rosalind.info/problems/perm/

Given: A positive integer n≤7.
Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
"""

def Permutation(n):
    import itertools
    list1 = []
    for i in range(n):
        list1.append(i + 1)
    list2 = list(itertools.permutations(list1, n))
    print(len(list2))
    for l in list2:
        print(" ".join([str(i) for i in l]))

if __name__ == "__main__":
    with open("../data/rosalind_perm.txt", "r") as f:
        n = int(f.readline().strip())
    Permutation(n)
