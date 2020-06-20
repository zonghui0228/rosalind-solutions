# ^_^ coding:utf-8 ^_^

# Semi-Connected Graph


# the input:
# A positive integer k≤20 and k simple directed graphs with at most 10**3 vertices each in the edge list format.
# ==============================
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
# print(graphs)


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
	matrix = [[False]*vertice for v in range(vertice)]
	for v in range(vertice):
		matrix[v][v] = True
	# print(matrix)
	# order, distance = BFS(1, vertice, graph)
	for v in range(vertice):
		order, distance = BFS(v+1, vertice, graph)
		# print(distance)
		for k in distance.keys():
			if distance[k] != -1:
				matrix[v][k-1] = True
				matrix[k-1][v] = True
	# print(matrix)
	for i in range(vertice):
		for j in range(vertice):
			if not matrix[i][j]:
				print(-1, end=" ")
				return -1
	print(1, end=" ")
	return 1


for i in range(k):
	graph = graphs[i]
	vertice = vertices[i]
	ifSemiConnectedGraph(graph, vertice)