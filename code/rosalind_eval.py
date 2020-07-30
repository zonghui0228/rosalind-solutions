# ^_^ coding:utf-8 ^_^

"""
Expected Number of Restriction Sites
url: http://rosalind.info/problems/eval/

Given: A positive integer n (n≤1,000,000), a DNA string s of even length at most 10, and an array A of length at most 20, containing numbers between 0 and 1.
Return: An array B having the same length as A in which B[i] represents the expected number of times that s will appear as a substring of a random DNA string t of length n, where t is formed with GC-content A[i] (see “Introduction to Random Strings”).
"""

with open("../data/rosalind_eval.txt", "r") as f:
    n = int(f.readline().strip())
    s = f.readline().strip()
    A = map(float, f.readline().strip().split(" "))

at = s.count('A') + s.count('T')
gc = s.count('G') + s.count('C')
for i in A:
    print(pow((1-i)/2, at) * pow(i/2, gc) * (n-len(s)+1), end=" ")
print()  
