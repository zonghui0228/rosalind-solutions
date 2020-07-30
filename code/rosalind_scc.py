# ^_^ coding:utf-8 ^_^

"""
Strongly Connected Components
url: http://rosalind.info/problems/scc/

Given: A simple directed graph with n≤103 vertices in the edge list format.
Return: The number of strongly connected components in the graph.
"""


# the input:
# A simple directed graph with n≤10**3 vertices in the edge list format.
# ==============================
data = "../data/rosalind_scc.txt"

with open(data, "r") as f:
	vertice, edge = map(int, f.readline().strip().split(" "))
	graph = {v:[] for v in range(1, vertice+1)}
	for line in f:
		vertice1, vertice2 = map(int, line.strip().split(" "))
		graph[vertice1].append(vertice2)
print(graph)
print(vertice)

# the solution:
# ==============================

def DFSUtil(graph, v, visited):
	visited[v] = True
	# print(v,)
	SCCs.append(v)
	for i in graph[v]:
		if visited[i] == False:
			DFSUtil(graph, i, visited)

def fillOrder(v, visited, stack):
	visited[v] = True
	for i in graph[v]:
		if visited[i]==False:
			fillOrder(i, visited, stack)
	stack.append(v)

def getTranspose(graph, vertice):
	gr = {v:[] for v in range(1, vertice+1)}
	for i in graph:
		for j in graph[i]:
			gr[j].append(i)
	return gr

def printSCCs(graph, vertice):
	stack = []
	visited = [False] * (vertice+1)
	for ve in range(1, vertice+1):
		if visited[ve]==False:
			fillOrder(ve, visited, stack)

	gr = getTranspose(graph, vertice)
	visited = [False] * (vertice+1)
	while stack:
		i = stack.pop()
		if visited[i]==False:
			DFSUtil(gr, i, visited)
			# print("")
			SCCs.append("")

SCCs = []
printSCCs(graph, vertice)
print(SCCs)
# print(SCCs.count(""))
