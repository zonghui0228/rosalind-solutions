# ^_^ coding:utf-8 ^_^

"""
Testing Bipartiteness
url: http://rosalind.info/problems/bip

Given: A positive integer k≤20 and k simple graphs in the edge list format with at most 103 vertices each.
Return: For each graph, output "1" if it is bipartite and "-1" otherwise.
"""

# the input
# ==============================
data = "../data/rosalind_bip.txt"
graphs = [] # 存储所有的graphs
vertices = [] # 存储所有的graphs的顶点数目
edges = [] # 存储所有的graphs的边数目

# 读取数据
with open(data, "r") as f:
    graph_count = int(f.readline().strip())

    for line in f:
        if line.strip():
            l = list(map(int, line.strip().split(" ")))
            graph[l[0]].append(l[1])
            graph[l[1]].append(l[0])

        else:
            # 获得顶点和边
            vertice, edge = map(int, f.readline().strip().split(" "))
            # 获得每个顶点的邻居点
            graph = {i+1:[] for i in range(vertice)}
            graphs.append(graph)
            vertices.append(vertice)
print(len(graphs))

# the solution:
# ==============================
# 深度优先搜索算法，只要所有相邻节点颜色不一致，就返回True，说明是Bipartiteness二分图。
def dfs_test_bip(graph, v, visited, color):
    for i in graph[v]:
        # print(v,i)
        if not visited[i]:
            visited[i] = True
            color[i] = not color[v]
            if (not dfs_test_bip(graph, i, visited, color)):
                return False
        else:
            if color[v] == color[i]:
                return False
    return True


for i in range(len(graphs)):
    graph = graphs[i] # 点及其邻居
    vertice = vertices[i] #顶点

    visited = [False for i in range(vertice+1)] # 记录该点是否被遍历过
    color = [False for i in range(vertice+1)] # 记录点的颜色
    visited[1] = True
    
    if dfs_test_bip(graph, 1, visited, color):
        print(1, end=" ")
    else:
        print(-1, end=" ")
