# ^_^ coding:utf-8 ^_^


# Breadth-First Search


# the input
# ==============================
data = "../data/rosalind_bfs.txt"
f = open(data, "r")
vertices, edges = f.readline().strip().split(" ")
directed_vertice_neighbors = {i+1:[] for i in range(int(vertices))}
for line in f:
	l = line.strip().split(" ")
	directed_vertice_neighbors[int(l[0])].append(int(l[1]))
f.close()


# the solution:
# ==============================
def BFS(start_vertice, vertices, directed_vertice_neighbors):
	quene, order = [], [] # quene存储需要进行遍历的数据， order存储遍历的路径
	distance = {i+1:0 for i in range(int(vertices))} # 初始化shortest path
	quene.append(start_vertice)
	order.append(start_vertice)
	# 进行广度优先遍历
	while quene:
		v = quene.pop(0)
		for n in directed_vertice_neighbors[v]:
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

start_vertice = 1
order, distance = BFS(start_vertice, vertices, directed_vertice_neighbors)
for i in range(int(vertices)):
	print(distance[i+1], end = " ")
