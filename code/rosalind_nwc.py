# ^_^ coding ^_^

"""
Negative Weight Cycle
url: http://rosalind.info/problems/nwc/

Given: A positive integer k≤20 and k simple directed graphs with integer edge weights from −103 to 103 and n≤103 vertices in the edge list format.
Return: For each graph, output "1" if it contains a negative weight cycle and "-1" otherwise.
"""

import sys

# the input:
# A positive integer k≤20 and k simple directed graphs with integer edge weights from −10**3 to 10**3 and n≤10**3 vertices in the edge list format.
# ==============================
data = "../data/rosalind_nwc.txt"
graphs = []
vertices = []
edges = []
negative_vertices=[]

with open(data, "r") as f:
    k = int(f.readline().strip())
    for line in f:
        if len(line.strip().split(" "))==3:
            vertice1, vertice2, weight = map(int, line.strip().split(" "))
            graph[vertice1][vertice2] = weight
            if weight < 0:
                negative_vertice.append(vertice1)

        else:
            vertice, edge = map(int, line.strip().split(" "))
            graph = {v:{} for v in range(1, vertice+1)}
            graphs.append(graph)
            vertices.append(vertice)
            edges.append(edge)
            negative_vertice = []
            negative_vertices.append(negative_vertice)
# print(graphs)


# the solustion:
# 使用BellmanFord算法, 如果有负权重环，那么环里一定含有负权重边的起点，因此对图里所有负权重环的起点，循环做BellmanFord算法寻找路径，并判断是否有负权重环。
# 若有任一负权重边起点，发现有负权重环存在，则返回True,输出1。若遍历完负权重边所有起点，都没负权重环，则返回-1。
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
                    # print("图包含具有负权重的圈")
                    return distance, True

    return distance, False

# Results:
for i in range(k):
    graph = graphs[i] # 图
    vertice = vertices[i] # 顶点
    negative_vertice = negative_vertices[i]
    flag = False
    for ve in negative_vertice: # 遍历所有节点，通过BellmanFord算法查询是否有负权重圈，若存在，则返回True，输出1
        distance, b = BellmanFord(graph, vertice, ve)
        if b:
            print(1, end=" ")
            flag=True
            break
    if not flag:
            print(-1, end=" ") # 遍历完所有节点后，都没有负权重圈，则输出-1


