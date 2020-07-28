# ^_^ coding:utf-8 ^_^

"""
Using the Spectrum Graph to Infer Peptides
url: http://rosalind.info/problems/sgra/

Given: A list L (of length at most 100) containing positive real numbers.
Return: The longest protein string that matches the spectrum graph of L (if multiple solutions exist, you may output any one of them). Consult the monoisotopic mass table.
"""

import numpy as np

mass_aa = {
        57.02146: "G", 71.03711: "A", 87.03203: "S", 97.05276: "P", 99.06841: "V",
        101.04768: "T", 103.00919: "C", 113.08406: "IL", 114.04293: "N", 115.02694: "D",
        128.05858: "Q", 128.09496: "K", 129.04259: "E", 131.04049: "M", 137.05891: "H",
        147.06841: "F", 156.10111: "R", 163.06333: "Y", 186.07931: "W"}

mass_aa_decimal2 = {round(k,2): v for k,v in mass_aa.items()}

# convert the l into graph and edges
def _get_graph(l):
    graph, edges = {}, {}
    for i in range(len(l)):
        graph[l[i]] = []
        for j in range(i, len(l)):
            aa = mass_aa_decimal2.get(round(l[j]-l[i], 2), 0)
            if aa:
               graph[l[i]].append(l[j])
               edges[(l[i],l[j])] = aa
    return graph, edges

# given a start and end of graph, return all path.
def dfs_find_all_path(graph, start, end, path=[]):
    path = path +[start]
    if start == end:
        return [path]
    paths = []  
    for node in graph[start]:
        if node not in path:
            newpaths = dfs_find_all_path(graph, node, end, path) 
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# ssing the spectrum graph to infer peptides
def _get_peptides(l, graph, edges):
    all_peptides_paths = []
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            all_paths = dfs_find_all_path(graph, l[i], l[j], path=[])
            all_peptides_paths.extend(all_paths)
    # print(all_peptides_paths)
    peptides = []
    for peptides_paths in  all_peptides_paths:
        peptide = [""]
        for i in range(len(peptides_paths)-1):
            aa = mass_aa_decimal2.get(round(peptides_paths[i+1] - peptides_paths[i], 2))
            peptide = [p+a for p in peptide for a in aa]
        peptides.extend(peptide)
    # print(peptides)
    return peptides

if __name__ == "__main__":
    # load data
    with open("../data/rosalind_sgra.txt", "r") as f:
        l = [float(line.strip()) for line in f]
    graph, edges = _get_graph(l)
    peptides = _get_peptides(l, graph, edges)
    longest_protein_string = max(peptides, key=len, default="")
    print(longest_protein_string)
