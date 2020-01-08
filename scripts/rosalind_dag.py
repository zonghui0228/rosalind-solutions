# ^_^ coding:utf-8 ^_^

# Testing Acyclicity


# the input
# ==============================
data = "../data/rosalind_dag.txt"
graphs = [] # 存储所有的graphs
vertices = [] # 存储所有的graphs的顶点数目
edges = [] # 存储所有的graphs的边数目
# 读取数据,有向图
with open(data, "r") as f:
	graph_count = int(f.readline().strip())

	for line in f:
		if line.strip():
			l = list(map(int, line.strip().split(" ")))
			graph[l[0]].append(l[1])

		else:
			# 获得顶点和边
			vertice, edge = map(int, f.readline().strip().split(" "))
			# 获得每个顶点的邻居点
			graph = {i+1:[] for i in range(vertice)}
			graphs.append(graph)
			vertices.append(vertice)
			edges.append(edge)
# print(graphs)
# print(vertices)
# print(edges)


# the solution:
# ==============================
# 使用dfs深度优先搜索，遍历所有顶点，如果从任何顶点出发搜索:
# 都不会回到遍历过得点，则认为无环，返回False; 
# 但凡有一次重新回到某个顶点，则认为有环，返回True.
def dfs(order, graph, v, visited):
	# print(graph, v, visited)
	if visited[v]:
		order.append(v)
		return True
	visited[v] = True
	order.append(v)

	for i in graph[v]:
		return(dfs(order, graph, i, visited))
	return False


def isDAG(graph, vertice):
	for v in range(1, vertice+1):
		visited = [False for i in range(int(vertice)+1)] # 记录该点是否被遍历过
		order = [] # 记录遍历路径，如果路径回到某个点，说明有环

		if dfs(order, graph, v, visited): #如果有环，输出-1；无环，输出1
			# print(order)
			# for o in order:
			# 	print(o, graph[o])
			return(-1)

	return(1)


for n in range(len(graphs)):
	graph = graphs[n]
	vertice = vertices[n]
	print(isDAG(graph, vertice), end=" ")


