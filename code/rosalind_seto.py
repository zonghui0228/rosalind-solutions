# ^_^ coding:utf-8 ^_^

"""
Introduction to Set Operations
url: http://rosalind.info/problems/seto/

Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.
Return: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set complements are taken with respect to {1,2,…,n}).
"""

# introduction to set operations.
def union(a, b):
    return a | b

def intersection(a, b):
    return a & b

def difference(a, b):
    return a - b

def set_complement(u, a):
    return u - a

def p(s):
    s = str(s).replace('set([', '')
    s = s.replace('])', '')
    return '{'+s+'}'

if __name__ == '__main__':
    with open("../data/rosalind_seto.txt", "r") as f:
        n = int(f.readline().strip())
        a0 = f.readline().strip()
        b0 = f.readline().strip()

    for i in ['{', '}']:
        a0 = a0.replace(i, '')
        b0 = b0.replace(i, '')

    a = set(int(i) for i in a0.split(', '))
    b = set([int(i) for i in b0.split(', ')])
    u = set({})
    for i in range(n):
        u.add(i+1)

    print(p(union(a,b)))
    print(p(intersection(a, b)))
    print(p(difference(a, b)))
    print(p(difference(b, a)))
    print(p(set_complement(u, a)))
    print(p(set_complement(u, b)))
