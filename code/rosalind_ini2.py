# ^_^ coding:utf-8 ^_^

"""
Variables and Some Arithmetic
url: http://rosalind.info/problems/ini2/

Given: Two positive integers a and b, each less than 1000.
Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.
"""

def hypotenuse_square(a, b):
    return a**2 + b**2

if __name__ == "__main__":
    with open("../data/rosalind_ini2.txt", "r") as f:
        l = f.readline().strip().split()
        a, b = int(l[0]), int(l[1])
    print(hypotenuse_square(a, b))