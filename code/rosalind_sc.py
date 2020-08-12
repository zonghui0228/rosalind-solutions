# ^_^ coding:utf-8 ^_^

"""
Semi-Connected Graph
url: http://rosalind.info/problems/sc/

Given: A positive integer k≤20 and k simple directed graphs with at most 103 vertices each in the edge list format.
Return: For each graph, output "1" if the graph is semi-connected and "-1" otherwise.
"""

import numpy as np

# the solution
# ==============================
def BFS(start_vertice, vertice, graph):
    quene, order = [], [] # quene存储需要进行遍历的数据， order存储遍历的路径
    distance = {i+1:0 for i in range(vertice)} # 初始化shortest path
    quene.append(start_vertice)
    order.append(start_vertice)
    # 进行广度优先遍历
    while quene:
        v = quene.pop(0)
        for n in graph[v]:
            if n not in order:
                distance[n] = distance[v] + 1
                order.append(n)
                quene.append(n)
    # 1无法到达的点，设置距离为-1
    for k in distance.keys():
        if k not in order:
            distance[k] = -1
    # 返回顺序，和距离
    return order, distance

def ifSemiConnectedGraph(graph, vertice):
    results = 1
    matrix = np.array([[0]*vertice for v in range(vertice)])
    for v in range(vertice):
        matrix[v][v] += 1

    for v in range(vertice):
        order, distance = BFS(v+1, vertice, graph)
        for k in distance.keys():
            if distance[k] != -1:
                matrix[v][k-1] += 1
                matrix[k-1][v] += 1
            else:
                matrix[v][k-1] -= 1
                matrix[k-1][v] -= 1
        matrix_flatten = matrix.flatten()
        if -2 in matrix_flatten:
            return -1
    return 1    

if __name__ == "__main__":
    # load data
    data = "../data/rosalind_sc.txt"
    graphs, vertices, edges = [], [], []
    with open(data, "r") as f:
        k = int(f.readline().strip())
        for line in f:
            if line.strip():
                vertice1, vertice2 = map(int, line.strip().split(" "))
                graph[vertice1].append(vertice2)

            else:
                vertice, edge = map(int, f.readline().strip().split(" "))
                vertices.append(vertice)
                edges.append(edge)
                graph = {v:[] for v in range(1, vertice+1)}
                graphs.append(graph)

    for i in range(k):
        graph = graphs[i]
        vertice = vertices[i]
        print(ifSemiConnectedGraph(graph, vertice))
