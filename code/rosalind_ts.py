# ^_^ coding:utf-8 ^_^

"""
Topological Sorting
url: http://rosalind.info/problems/ts/

Given: A simple directed acyclic graph with n≤103 vertices in the edge list format.
Return: A topological sorting (i.e., a permutation of vertices) of the graph.
"""

from collections import defaultdict

# the input
# ==============================
data = "../data/rosalind_ts.txt"
with open(data, "r") as f:
    vertice, edge = map(int, f.readline().strip().split(" "))
    graph = defaultdict(list)
    for line in f:
        vertice1, vertice2 = map(int, line.strip().split(" "))
        graph[vertice1].append(vertice2)
# print(vertice, edge)
# print(graph)


# the solution
# ==============================
def topologicalsortUtil(v, visited, stack):
    visited[v] = True
    for i in graph[v]:
        if visited[i]==False:
            topologicalsortUtil(i, visited, stack)
    stack.insert(0, v)

def topologicalsort(graph, vertice):
    visited = [False] * (vertice+1) # 我们的点有0，因此visited长度设为v+1
    stack = [] # 保存topological sort结果

    for v in range(1, vertice+1):
        if visited[v]==False:
            topologicalsortUtil(v, visited, stack)
    return(stack)

stack = topologicalsort(graph, vertice)
for i in stack:
    print(i, end=" ")

# reference:
# 1. https://www.runoob.com/python3/python-topological-sorting.html
