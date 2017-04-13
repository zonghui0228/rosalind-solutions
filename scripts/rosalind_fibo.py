# coding: utf-8
# 斐波那契数列 
def fibonacci_number(n):
	if n == 0: return 0
	elif n == 1: return 1
	elif n > 1: return fibonacci_number(n - 1) + fibonacci_number(n - 2)

# print fibonacci_number(25)