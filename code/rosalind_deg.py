# ^_^ coding:utf-8 ^_^

"""
Degree Array
url: http://rosalind.info/problems/deg/

Given: A simple graph with n≤103 vertices in the edge list format.
Return: An array D[1..n] where D[i] is the degree of vertex i.
"""

# the input:
# ==============================
data = "../data/rosalind_deg.txt"

# the solution:
# ==============================
edge_list = []
with open(data, "r") as f:
    nodes, edges = f.readline().strip().split(" ")
    for line in f:
        edge_list.extend([int(i) for i in line.strip().split(" ")])

degrees = []
for i in range(int(nodes)):
    degrees.append(str(edge_list.count(i+1)))
print(" ".join(degrees))
