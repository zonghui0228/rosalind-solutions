# ^_^ coding:utf-8 ^_^

"""
Bellman-Ford Algorithm
url: http://rosalind.info/problems/bf

Given: A simple directed graph with integer edge weights from −103 to 103 and n≤103 vertices in the edge list format.
Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). If i is not reachable from 1 set D[i] to x.
"""

import sys

# the input:
# A simple directed graph with integer edge weights from −10**3 to 10**3 and n≤10**3 vertices in the edge list format.
# ==============================
data = "../data/rosalind_bf.txt"
with open(data, "r") as f:
	vertice, edge = map(int, f.readline().strip().split(" "))
	graph = {v:{} for v in range(1, vertice+1)}
	for line in f:
		vertice1, vertice2, weight = map(int, line.strip().split(" "))
		graph[vertice1][vertice2] = weight
# print(vertice, edge)
# print(graph)


# the solution:
# 使用BellmanFord算法
# ==============================
def BellmanFord(graph, vertice, source):
	# 初始化
	distance = {i:sys.maxsize for i in graph} # 初始设置为代表无穷大
	predecessor = {i:None for i in graph}
	distance[source] = 0 # 到原点距离设置为0

	# 对每一条边重复操作
	for i in range(vertice-1):
		for u in graph:
			if distance[u] != sys.maxsize:
				for v in graph[u]:
					if distance[v] > distance[u] + graph[u][v]:
						distance[v] = distance[u] + graph[u][v]
						predecessor[v] = u
	
	# 检查是否有负权重的边
	for u in graph:
		if distance[u] != sys.maxsize:
			for v in graph[u]:
				if distance[v] > distance[u] + graph[u][v]:
					print("with negative cycles")

	return distance, predecessor
distance, predecessor = BellmanFord(graph, vertice, 1)

# results:
for i in graph:
	if distance[i] == sys.maxsize:
		print("x", end=" ")
	else:
		print(distance[i], end = " ")
