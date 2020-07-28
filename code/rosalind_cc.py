# ^_^ coding ^_^

"""
Connected Components
url: http://rosalind.info/problems/cc/

Given: A simple graph with n≤10**3 vertices in the edge list format.
Return: The number of connected components in the graph.
"""

# the input
# ==============================
data = "../data/rosalind_cc.txt"
f = open(data, "r")
# 获得顶点和边
vertice, edge = map(int, f.readline().strip().split(" "))
# 获得每个顶点的邻居点
graph = {i+1:[] for i in range(vertice)}
for line in f:
    l = list(map(int, line.strip().split(" ")))
    graph[l[0]].append(l[1])
    graph[l[1]].append(l[0])
f.close()

# the solution
# ==============================
# 深度优先搜索算法
def dfs(cc, v, visited):
    visited[v] = True
    cc.append(v)
    for i in graph[v]:
        if visited[i] == False:
            cc = dfs(cc, i, visited)
    return cc

visited = [False for i in range(vertice+1)] # 记录该点是否被遍历过
connected_components = [] # 记录联通分支，connected component
for v in range(1, int(vertice)+1):
    if visited[v] == False:
        cc = []
        connected_components.append(dfs(cc, v, visited))

# 结果：
# print(connected_components)
print("results: {}".format(len(connected_components)))
