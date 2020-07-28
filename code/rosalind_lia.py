# ^_^ coding:utf-8 ^_^

"""
Independent Alleles
url: http://rosalind.info/problems/lia/

Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.
Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
"""

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f  = f *i
    return f

def combination(i, j):
    return factorial(i)/(factorial(j) * factorial(i - j))

def independent_alleles(k, n):
    print('孟德尔第二定律')
    print('第0代只有tom一人，每个后代都会生两个孩子，每个配偶都会是AaBb,求第k代至少有n个AaBb的后代的概率')
    print('第k代是AaBb的概率是0.25')
    p = 0
    count = pow(2, k)                        # count 为第k代人数
    for i in range(n, count+1):
        p += combination(count, i) * pow(0.25, i) * pow(0.75, count - i)
    return p

if __name__ == "__main__":
    with open("../data/rosalind_lia.txt", "r") as f:
        k, n = [int(i) for i in f.readline().strip().split(" ")]
    print(independent_alleles(k,n))