# ^_^ coding:utf-8 ^_^

# Dijkstra's Algorithm
import numpy as np
import sys


# the input
# ==============================
data = "../data/rosalind_dij.txt"

with open(data, "r") as f:
	vertice, edge = map(int, f.readline().strip().split(" "))
	# graph = np.zeros((vertice, vertice), dtype=int) # 错误示范，有向图里未连通的点之间距离为0，这是错误的
	graph = [[sys.maxsize] *vertice for i in range(vertice)] # 正确示范，有向图里未连通的点之间距离应该为无穷大
	for line in f:
		node1, node2, weight = map(int, line.strip().split(" "))
		graph[node1-1][node2-1] = weight
		# graph[node2-1][node1-1] = weight
# print(graph)


# the solution
# ==============================
def minDistance(dist, visited):
	mini = sys.maxsize
	mini_index = dist.index(mini)
	# 通过循环，获得当前dist里面未被处理的点中，距离最小的那个。
	for v in range(vertice):
		if dist[v] < mini and visited[v] == False:
			mini = dist[v]
			mini_index = v
	return mini_index

def dijkstra(src, graph, vertice):
	dist = [sys.maxsize] * vertice # 用来存储距离，初始都为无穷大
	dist[src] = 0 # 与自己的距离设置为0
	visited = [False] * vertice # 记录是否已经获得该点的最小距离

	for c in range(vertice):
		u = minDistance(dist, visited) #这是还未被处理的点里，dis最小的点
		visited[u] = True

		for v in range(vertice):
			if graph[u][v]>0 and visited[v]==False and dist[v] > dist[u]+graph[u][v]: # u-v有向，v未被访问，到v更长，
				dist[v] = dist[u] + graph[u][v] # 更新v

	for n in range(vertice):
		# print(n, '\t', dist[n])

		if dist[n] < sys.maxsize:
			print(dist[n], end=" ")
		else:
			print(-1, end=" ")

dijkstra(0, graph, vertice)
# print(sys.maxsize)

# reference urls:
# 1. https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
# 2. https://www.jianshu.com/p/d69097812d56