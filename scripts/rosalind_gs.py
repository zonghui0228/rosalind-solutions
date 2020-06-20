# ^_^ coding:utf-8 ^_^

# General Sink


# the input:
# A positive integer k≤20 and k simple directed graphs with at most 10**3 vertices and 2*10**3 edges each in the edge list format.
# ==============================
data = "../data/rosalind_gs.txt"
graphs = []
vertices = []
edges = []

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
# print(graphs)


# the solution:
# ==============================
# 使用深度优先搜索，
def DFS(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i]==False:
            DFS(graph, i, visited)

def findMother(graph, vertice):
    visited = [False] * (vertice+1)
    # To store last finished vertex (or mother vertex)
    v = 1
    # Do a DFS traversal and find the last finished vertex
    for i in range(1, vertice+1):
        if visited[i]==False:
            DFS(graph, i, visited)
            v = i
            
    visited = [False] * (vertice+1)
    DFS(graph, v, visited)

    if any(i==False for i in visited[1:]):
        return -1
    else:
        return v

# the Results:
for n in range(k):
    graph = graphs[n]
    vertice = vertices[n]
    print(findMother(graph, vertice), end=" ")


# the reference url:
# 1. https://www.geeksforgeeks.org/find-a-mother-vertex-in-a-graph/