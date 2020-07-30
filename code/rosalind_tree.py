# ^_^ coding:utf-8 ^_^

"""
Completing a Tree
url: http://rosalind.info/problems/tree/

Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.
Return: The minimum number of edges that can be added to the graph to produce a tree.
"""

# the input:
# ==============================
data = "../data/rosalind_tree.txt"

# the solution:
# ==============================
with open(data, "r") as f:
    n = int(f.readline())
    adjacency_list = [line.strip().split(" ") for line in f]
# print(n)
# print(adjacency_list)

subtrees = [] # 能连接在一起的树
nodes = set() # 已经有边的点
for i, j in adjacency_list:
    if i in nodes or j in nodes:
        for st in subtrees:
            if i in st or j in st:
                subtrees[subtrees.index(st)].append(i)
                subtrees[subtrees.index(st)].append(j)
                nodes.add(i), nodes.add(j)
    else:
        subtrees.append([i,j])
        nodes.add(i), nodes.add(j)

l = len(subtrees)
for i in range(l):
    for j in range(l):
        if i==j:
           break
        if len(set(subtrees[i] + subtrees[j])) < len(subtrees[i]) + len(subtrees[j]):
            subtrees[i] = list(set(subtrees[i] + subtrees[j]))
            subtrees[j] = []
subtrees = [i for i in subtrees if i]
# print(subtrees)
# print(nodes)

result = (n -len(nodes)) + len(subtrees) - 1
print(result)
