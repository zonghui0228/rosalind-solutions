# coding: utf-8

"""
Fibonacci Numbers
url: http://rosalind.info/problems/fibo/

Given: A positive integer n≤25.
Return: The value of Fn.
"""

# 斐波那契数列 
def fibonacci_number(n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n > 1: return fibonacci_number(n - 1) + fibonacci_number(n - 2)
# print(fibonacci_number(6))

if __name__ == "__main__":
    with open("../data/rosalind_fibo.txt", "r") as f:
        n = int(f.readline().strip())
        print(fibonacci_number(n))