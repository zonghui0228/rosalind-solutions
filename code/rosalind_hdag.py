# ^_^ codig:utf-8 ^_^

"""
Hamiltonian Path in DAG
url: http://rosalind.info/problems/hgad/

Given: A positive integer k≤20 and k simple directed acyclic graphs in the edge list format with at most 103 vertices each.
Return: For each graph, if it contains a Hamiltonian path output "1" followed by a Hamiltonian path (i.e., a list of vertices), otherwise output "-1".
"""

# the input:
# A positive integer k≤20 and k simple directed acyclic graphs in the edge list format with at most 10**3 vertices each.
# ==============================
data = "../data/rosalind_hdag.txt"

graphs = [] # 存储所有的graphs
vertices = [] # 存储所有的graphs的顶点数目
edges = [] # 存储所有的graphs的边数目
with open(data, "r") as f:
    k = int(f.readline().strip())
    for line in f:
        if line.strip():
            vertice1, vertice2 = list(map(int, line.strip().split(" ")))
            graph[vertice1].append(vertice2)
        else:
            # 获得顶点和边
            vertice, edge = map(int, f.readline().strip().split(" "))
            # 获得每个顶点的邻居点
            graph = {v:[] for v in range(1, vertice+1)}
            graphs.append(graph)
            vertices.append(vertice)
            edges.append(edge)
# print(graphs)


# the solution:
# ==============================
# 先对DAG进行拓扑排序，而后检查拓扑排序后的list的连续性，保证list中相邻点在graph中有边
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

def check_consecutive(stack, graph):
    for i in range(len(stack)-1):
        if stack[i+1] not in graph[stack[i]]:
            return False
    return True

# the results:
for n in range(k):
    graph = graphs[n]
    vertice = vertices[n]
    stack = topologicalsort(graph, vertice)
    if check_consecutive(stack, graph):
        print(1, end=" ")
        for i in stack:
            print(i, end=" ")
        print("")
    else:
        print(-1)
