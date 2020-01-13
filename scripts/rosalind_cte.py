# ^_^ coding:utf-8 ^_^

# Shortest Cycle Through a Given Edge
import numpy as np
import sys


# the input:
# A positive integer k≤20 and k simple directed graphs with positive integer edge weights and at most 10**3 vertices in the edge list format
# ==============================
data = "../data/rosalind_cte.txt"

graphs = [] # 存储所有的graphs
vertices = [] # 存储所有的graphs的顶点数目
edges = [] # 存储所有的graphs的边数目
first_specified_edges = []
# 读取数据,有向图
with open(data, "r") as f:
	k = int(f.readline().strip())

	for line in f:
		# print(line)
		if len(line.strip().split(" "))==3:
			vertice1, vertice2, weight = list(map(int, line.strip().split(" ")))
			graph[vertice1][vertice2] = weight

		else:
			# 获得顶点和边
			vertice, edge = map(int, line.strip().split(" "))
			# 获得每个顶点的邻居点
			graph = {v:{} for v in range(1, vertice+1)}
			graphs.append(graph)
			vertices.append(vertice)
			edges.append(edge)
			first_specified_edges.append(list(map(int, f.readline().strip().split(" "))))
# print(graphs)
# print(vertices)
# print(edges)
# print(first_specified_edges)


# the solution:
# 在此处我们使用BellmanFord算法寻找有向权重图的最短距离，首先把first_specified_edge这条边不计入图，
# 其次寻找first_specified_edge的第2个点到第1个点的最短距离，若存在，则加上这两点的权重，就为我们的结果；若不存在，则返回-1
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
					print("without negative cycles")

	return distance, predecessor

# the results:
for n in range(k):
	graph = graphs[n]
	vertice = vertices[n]
	first_specified_edge = first_specified_edges[n]
	distance, predecessor = BellmanFord(graph, vertice, first_specified_edge[1])
	# print(distance)
	if distance[first_specified_edge[0]] == sys.maxsize:
		print(-1, end=" ")
	else:
		print(distance[first_specified_edge[0]]+first_specified_edge[2], end=" ")

