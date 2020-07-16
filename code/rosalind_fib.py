# python3

# Given: Positive integers  and .
# Return: The total number of rabbit pairs that will be present after  months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of  rabbit pairs (instead of only 1 pair).

def fib(n, k):
	if n <= 2:
		return 1
	else:
		return fib(n-1,k) + k * fib(n-2,k)


if __name__ == "__main__":
	with open("../data/rosalind_fib.txt", 'r') as f:
		n, k = f.readline().strip().split(" ")
		print(fib(int(n), int(k)))


