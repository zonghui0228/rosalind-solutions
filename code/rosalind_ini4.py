# ^_^ coding:utf-8 ^_^

"""
Conditions and Loops
url: http://rosalind.info/problems/ini4/

Given: Two positive integers a and b (a<b<10000).
Return: The sum of all odd integers from a through b, inclusively.
"""

def odd_sum(a, b):
    return sum([i for i in range(a, b+1) if i%2==1])

if __name__ == "__main__":
    with open("../data/rosalind_ini4.txt", "r") as f:
        a, b = map(int, f.readline().strip().split())
    print(odd_sum(a, b))
    