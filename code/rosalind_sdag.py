# ^_^ coding:utf-8 ^_^

"""
Shortest Paths in DAG
url: http://rosalind.info/problems/sdag/

Given: A weighted DAG with integer edge weights from −103 to 103 and n≤105 vertices in the edge list format.
Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). If i is not reachable from 1 set D[i] to x.
"""

import sys

# the input:
# A weighted DAG with integer edge weights from −10**3 to 10**3 and n≤10**5 vertices in the edge list format.
# ==============================
data = "../data/rosalind_sdag.txt"
with open(data, "r") as f:
    vertice, edge = map(int, f.readline().strip().split(" "))
    graph = {v:{} for v in range(1, vertice+1)}
    for line in f:
        vertice1, vertice2, weight = map(int, line.strip().split(" "))
        graph[vertice1][vertice2] = weight
# print(vertice, edge)
# print(graph)

# the solution:
# 对于DAG,先计算拓扑排血，而后再计算距离
# ==============================
def topologicalSort(v, visited, stack):
    """拓扑排序"""
    visited[v] = True
    for u in graph[v]:
        if visited[u]==False:
            topologicalSort(u, visited, stack)
    stack.append(v)

def shortestPath(graph, vertice, source):
    # 初始化
    visited = [False] * (vertice+1)
    # 拓扑排序
    stack = []

    for i in range(1, vertice+1):
        if visited[i]==False:
            topologicalSort(i, visited, stack)
    # print(stack)

    # 距离
    distance = [sys.maxsize] * (vertice+1)
    distance[source] = 0

    while stack:
        # Get the next vertex from topological order
        i = stack.pop()
        # Update distances of all adjacent vertices
        for u in graph[i]:
            if distance[i]!=sys.maxsize and distance[u] > distance[i] + graph[i][u]:
                distance[u] = distance[i] + graph[i][u]
    return distance
distance = shortestPath(graph, vertice, 1)

# Results:
for i in graph:
    if distance[i] == sys.maxsize:
        print("x", end=" ")
    else:
        print(distance[i], end = " ")

# Reference url:
# 1. https://www.geeksforgeeks.org/shortest-path-for-directed-acyclic-graphs/