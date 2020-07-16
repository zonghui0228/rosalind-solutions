# coding: utf - 8
# Given: Integers n and m, followed by an n × (m+1) matrix Down 
# and an (n+1) × m matrix Right. The two matrices are separated by the "-" symbol.

# Return: The length of a longest path from source (0, 0) to sink (n, m) in the 
# n × m rectangular grid whose edges are defined by the matrices Down and Right.


def LongestPath(n, m, down, right):
	result = [[0] * (m+1) for i in range(n+1)]
# result = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
	for i in range(1,n+1):
		result[i][0] = result[i-1][0] + int(down[i-1][0])
# result = [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [5, 0, 0, 0, 0], [9, 0, 0, 0, 0], [14, 0, 0, 0, 0]]
	for j in range(1,m+1):
		result[0][j] = result[0][j-1] + int(right[0][j-1])
# result = [[0, 3, 5, 9, 9], [1, 0, 0, 0, 0], [5, 0, 0, 0, 0], [9, 0, 0, 0, 0], [14, 0, 0, 0, 0]]
	for i in range(1,n+1):
		for j in range(1,m+1):
			# print i,j,down[i-1][j],right[i][j-1]
			result[i][j] = max(result[i-1][j] + int(down[i-1][j]), result[i][j-1] + int(right[i][j-1]))
	return result[n][m]






fp = open("rosalind_BA5B.txt")
filelist = []
down = []
right = []
for line in fp.readlines():
	filelist.append(line.strip())
# print filelist
n = int(filelist[1].split(' ')[0])
# print n
m = int(filelist[1].split(' ')[1])
# print m
for i in range(2, 2 + n):
	down.append(filelist[i].replace(' ',''))
# print down
for j in range(3 + n, 2 * n + 4):
	right.append(filelist[j].replace(' ',''))
# print right
fp.close()
# print LongestPath(n,m,down,right)
