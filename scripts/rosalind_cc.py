# ^_^ coding ^_^

# Connected Components


# the input
# ==============================
data = "../data/rosalind_cc.txt"
f = open(data, "r")
# 获得顶点和边
vertices, edges = f.readline().strip().split(" ")
# 获得每个顶点的邻居点
vertice_neighbors = {i+1:[] for i in range(int(vertices))}
for line in f:
	l = line.strip().split(" ")
	vertice_neighbors[int(l[0])].append(int(l[1]))
	vertice_neighbors[int(l[1])].append(int(l[0]))
f.close()


# the solution
# ==============================
# 深度优先搜索算法
def dfs(cc, v, visited):
	visited[v] = True
	cc.append(v)
	for i in vertice_neighbors[v]:
		if visited[i] == False:
			cc = dfs(cc, i, visited)
	return cc

visited = [False for i in range(int(vertices)+1)] # 记录该点是否被遍历过
connected_components = [] # 记录联通分支，connected component
for v in range(1, int(vertices)+1):
	if visited[v] == False:
		cc = []
		connected_components.append(dfs(cc, v, visited))

# 结果：
# print(connected_components)
print("results: {}".format(len(connected_components)))
