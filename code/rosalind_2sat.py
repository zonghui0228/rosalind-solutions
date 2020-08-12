# ^_^ coding ^_^

"""
2-Satisfiability
http://rosalind.info/problems/2sat/

Given: A positive integer k≤20 and k 2SAT formulas represented as follows. The first line gives the number of variables n≤103 and the number of clauses m≤104, each of the following m lines gives a clause of length 2 by specifying two different literals: e.g., a clause (x3∨x¯¯¯5) is given by 3 -5.
Return: For each formula, output 0 if it cannot be satisfied or 1 followed by a satisfying assignment otherwise.
"""


# the input:
# ==============================
data = "../data/rosalind_2sat.txt"
graphs = []
graphs_t = []
variables = []
clauses = []
with open(data, "r") as f:
    k = int(f.readline().strip())
    for line in f:
        if line.strip():
            a, b = map(int, line.strip().split(" "))
            if a>0 and b>0:
                # graph[2*abs(a)-2].append(2*abs(b)-1)
                graph[2*abs(a)-1].append(2*abs(b)-2) #a-, b
                graph[2*abs(b)-1].append(2*abs(a)-2) #b-, a
                # graph[2*abs(b)-2].append(2*abs(a)-1)
                graph_t[2*abs(b)-2].append(2*abs(a)-1)
                graph_t[2*abs(a)-2].append(2*abs(b)-1)
            elif a<0 and b>0:
                # graph[2*abs(a)-1].append(2*abs(b)-1)
                graph[2*abs(a)-2].append(2*abs(b)-2) #a-, b
                graph[2*abs(b)-1].append(2*abs(a)-1) #b-, a
                # graph[2*abs(b)-2].append(2*abs(a)-2)
                graph_t[2*abs(b)-2].append(2*abs(a)-2)
                graph_t[2*abs(a)-1].append(2*abs(b)-1)
            elif a>0 and b<0:
                # graph[2*abs(a)-2].append(2*abs(b)-2)
                graph[2*abs(a)-1].append(2*abs(b)-1) #a-, b
                graph[2*abs(b)-2].append(2*abs(a)-2) #b-, a
                # graph[2*abs(b)-1].append(2*abs(a)-1)
                graph_t[2*abs(b)-1].append(2*abs(a)-1)
                graph_t[2*abs(a)-2].append(2*abs(b)-2)
            else:
                # graph[2*abs(a)-1].append(2*abs(b)-2)
                graph[2*abs(a)-2].append(2*abs(b)-1) #a-, b
                graph[2*abs(b)-2].append(2*abs(a)-1) #b-, a
                # graph[2*abs(b)-1].append(2*abs(a)-2)
                graph_t[2*abs(b)-1].append(2*abs(a)-2)
                graph_t[2*abs(a)-1].append(2*abs(b)-2)
        else:
            variable, clause = map(int, f.readline().strip().split(" "))
            variables.append(variable)
            clauses.append(clause)
            graph = {v:[] for v in range(2*variable)}
            graphs.append(graph)
            graph_t = {v:[] for v in range(2*variable)}
            graphs_t.append(graph_t)
print(graphs)
print(graphs_t)
print(variables)
print(clauses)


# the solution:
# ==============================
def dfs1(v, used, order):
    used[v] = True
    for u in graph[v]:
        if not used[u]:
            dfs1(u, used, order)
    order.append(v)

def dfs2(v, cl, comp, used_t, graph_t):
    used_t[v] = True
    for u in graph_t[v]:
        if not used_t[u]:
            dfs2(u, cl, comp, used_t, graph_t)
    comp[v] = cl

def solve_2sat(n, graph, graph_t):
    order = []
    used = [False] * n
    # print(n, len(graph))
    for i in range(n):
        if not used[i]:
            dfs1(i, used, order)
    # print(order)

    comp = [-1] * n
    j = 1
    used_t = [False] * n
    for i in range(n):
        v = order[n-i-1]
        if not used_t[v]:
            dfs2(v, j, comp, used_t, graph_t)
            j += 1

    assignment = [False] * int(n/2)
    # print(assignment)
    for i in range(0, n, 2):
        if comp[i] == comp[i+1]:
            print(0)
            return False
        assignment[int(i/2)] = comp[i] > comp[i+1]

    # output results:
    # print(assignment)
    print(1, end=" ")
    for i in range(len(assignment)):
        if assignment[i]:
            print(i+1, end=" ")
        else:
            print(-(i+1), end=" ")
    return True

# the results:
# for i in range(k):
#     graph = graphs[i]
#     graph_t = graphs_t[i]
#     variable = variables[i]
#     solve_2sat(variable*2, graph, graph_t)

# reference url:
# 1. https://cp-algorithms.com/graph/2SAT.html
# 2. https://www.geeksforgeeks.org/2-satisfiability-2-sat-problem/