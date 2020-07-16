# python3


# Given: Three positive integers , , and , representing a population containing  organisms:  individuals are homozygous dominant for a factor,  are heterozygous, and  are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.


def iprb(k, m, n):
	i = m * m + 4 * n * n + 4 * m * n - 4 * n - m
	j = 4 * (k + m + n) * (k + m + n - 1)
	rst = 1 - float(i) / j
	return rst


if __name__ == "__main__":
	with open("../data/rosalind_iprb.txt", 'r') as f:
		k, m, n = f.readline().strip().split(" ")
		print(iprb(int(k), int(m), int(n)))