# coding: utf-8
# Merge Two Sorted Arrays
def merge_sort(A, B):
	C = []
	i, j = 0, 0
	while i < len(A) and j < len(B):
		if A[i] <= B[j]:
			C.append(A[i])
			i += 1
		else:
			C.append(B[j])
			j += 1
	# 最后一项即最大值，在下一步写入
	C += A[i:]
	C += B[j:]
	return C

# 下述if语句在直接执行该函数时，True,可运行，在调用该模块时，默认__name__等于py文件名，所以不可运行，秒！
if __name__ == '__main__':
	import linecache
	A = [ int(n) for n in linecache.getline('rosalind_mer.txt', 2).strip().split(' ')]
	B = [ int(n) for n in linecache.getline('rosalind_mer.txt', 4).strip().split(' ')]
	for i in merge_sort(A, B):
		print i,