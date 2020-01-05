# ^_^ coding:utf-8 ^_^


# Breadth-First Search


# the input
# ==============================
data = "../data/rosalind_bfs.txt"
f = open(data, "r")
nodes, edges = f.readline().strip().split(" ")
directed_neighbor_nodes = {str(i+1):[] for i in range(int(nodes))}
for line in f:
	l = line.strip().split(" ")
	directed_neighbor_nodes[l[0]].append(l[1])
f.close()


# the solution:
# ==============================
def BFS(start_node, nodes, directed_neighbor_nodes):
	quene, order = [], [] # quene存储需要进行遍历的数据， order存储遍历的路径
	distance = {str(i+1):0 for i in range(int(nodes))} # 初始化shortest path
	quene.append(start_node)
	order.append(start_node)
	# 进行广度优先遍历
	while quene:
		v = quene.pop(0)
		for n in directed_neighbor_nodes[v]:
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

start_node = "1"
order, distance = BFS(start_node, nodes, directed_neighbor_nodes)
for i in range(int(nodes)):
	print(distance[str(i+1)], end = " ")
