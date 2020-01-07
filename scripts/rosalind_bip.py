# ^_^ coding:utf-8 ^_^

# testing bipartiteness


# the input
# ==============================
data = "../data/rosalind_bip.txt"
graphs_vertice_neighbors = [] # 存储graph的点及其邻居
graphs_vertices = [] # 存储graphs的顶点数目
# 读取数据
with open(data, "r") as f:
	graph_numbers = int(f.readline().strip())

	for line in f:
		if line.strip():
			l = line.strip().split(" ")
			vertice_neighbors[int(l[0])].append(int(l[1]))
			vertice_neighbors[int(l[1])].append(int(l[0]))

		else:
			# 获得顶点和边
			vertices, edges = f.readline().strip().split(" ")
			# 获得每个顶点的邻居点
			vertice_neighbors = {i+1:[] for i in range(int(vertices))}
			graphs_vertice_neighbors.append(vertice_neighbors)
			graphs_vertices.append(vertices)
print(len(graphs_vertice_neighbors))


# the solution:
# ==============================
# 深度优先搜索算法，只要所有相邻节点颜色不一致，就返回True，说明是Bipartiteness二分图。
def dfs_test_bip(vertice_neighbors, v, visited, color):
	for i in vertice_neighbors[v]:
		# print(v,i)
		if not visited[i]:
			visited[i] = True
			color[i] = not color[v]
			if (not dfs_test_bip(vertice_neighbors, i, visited, color)):
				return False
		else:
			if color[v] == color[i]:
				return False
	return True


for i in range(len(graphs_vertice_neighbors)):
	vertice_neighbors = graphs_vertice_neighbors[i] # 点及其邻居
	vertices = graphs_vertices[i] #顶点

	visited = [False for i in range(int(vertices)+1)] # 记录该点是否被遍历过
	color = [False for i in range(int(vertices)+1)] # 记录点的颜色
	visited[1] = True
	
	if dfs_test_bip(vertice_neighbors, 1, visited, color):
		print(1, end=" ")
	else:
		print(-1, end=" ")
