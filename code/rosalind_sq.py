# ^_^ coding:utf-8 ^_^

"""
Square in a Graph
url: http://rosalind.info/problems/sq/

Given: A positive integer k≤20 and k simple undirected graphs with n≤400 vertices in the edge list format.
Return: For each graph, output "1" if it contains a simple cycle (that is, a cycle which doesn’t intersect itself) of length 4 and "-1" otherwise.
"""

import numpy as np

# the input
# =================================
data = "../data/rosalind_sq.txt"
graphs = [] # 存储所有的graphs
vertices = [] # 存储所有的graphs的顶点数目
edges = [] # 存储所有的graphs的边数目
# 读取数据,有向图
with open(data, "r") as f:
    graph_count = int(f.readline().strip())

    for line in f:
        if line.strip():
            l = list(map(int, line.strip().split(" ")))
            graph[l[0]-1][l[1]-1] = 1
            graph[l[1]-1][l[0]-1] = 1

        else:
            # 获得顶点和边
            vertice, edge = map(int, f.readline().strip().split(" "))
            # 获得每个顶点的邻居点
            graph = np.zeros((vertice, vertice), dtype=int)
            graphs.append(graph)
            vertices.append(vertice)
            edges.append(edge)
# print(graphs)
# print(vertices)
# print(edges)


# the solution
# =================================
def DFS(graph, visited, n, vert, start, count):
    visited[vert] = True

    # 如果长度为n-1的path找到了
    if n==0:
        visited[vert] = False
        if graph[vert][start] == 1:
            count += 1
            return count
        else:
            return count
    for i in range(v):
        if visited[i]==False and graph[vert][i]==1:
            count = DFS(graph, visited, n-1, i, start, count)
    visited[vert] = False
    return count


def countCycles(graph, n):
    # 记录是否已经搜索过
    visited = [False] * v

    count = 0
    for i in range(v-(n-1)):
        count = DFS(graph, visited, n-1, i, i, count)
        visited[i] = True

    # 每个cycle都被计算了两次，所以除以2
    return int(count/2)

for g in range(graph_count):
    # number of vertices 
    v = vertices[g]
    # length of cycles
    n = 4 
    # graph
    graph = graphs[g]

    if countCycles(graph, n) > 0:
        print(1, end=" ")
    else:
        print(-1, end=" ")

# reference urls
# 1. https://www.geeksforgeeks.org/cycles-of-length-n-in-an-undirected-and-connected-graph/
