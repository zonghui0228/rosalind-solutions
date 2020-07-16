# coding:utf-8
# Independent Alleles
# Mendel's Second Law

# Sample Dataset
# 2, 1
# Sample Output
# 0.684

# n的阶乘
def factorial(n):
	f = 1
	for i in range(1, n+1):
		f  = f *i
	return f
# print factorial(4)

# 组合C(i, j)
def combination(i, j):
	return factorial(i)/(factorial(j) * factorial(i - j))

# print combination(5, 3)

def independent_alleles(k, n):
	print '孟德尔第二定律'
	print '第0代只有tom一人，每个后代都会生两个孩子，每个配偶都会是AaBb,求第k代至少有n个AaBb的后代的概率'
	print '第k代是AaBb的概率是0.25'
	p = 0
	count = pow(2, k)                        # count 为第k代人数
	for i in range(n, count+1):
		p += combination(count, i) * pow(0.25, i) * pow(0.75, count - i)
	return p
print independent_alleles(7,37)