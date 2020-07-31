# ^_^ coding:utf-8 ^_^

"""
Introduction to Pattern Matching
url: http://rosalind.info/problems/trie/

Given: A list of at most 100 DNA strings of length at most 100 bp, none of which is a prefix of another.
Return: The adjacency list corresponding to the trie T for these patterns, in the following format. If T has n nodes, first label the root with 1 and then label the remaining nodes with the integers 2 through n in any order you like. Each edge of the adjacency list of T will be encoded by a triple containing the integer representing the edge's parent node, followed by the integer representing the edge's child node, and finally the symbol labeling the edge.
"""

def get_most_overlap(s, L):
    most_string, most_overlap = "", ""
    for l in L:     
        overlap = ""
        for i in range(len(s)):
            if l[:len(s)-i] == s[:len(s)-i]:
                overlap = l[:len(s)-i]
                break
        if len(overlap) > len(most_overlap):
            most_string = l
            most_overlap = overlap
    return most_string, most_overlap

def get_adjacency_dict(strings):
    n = 1
    visited_string = []
    adjacency_dict = {}

    for s in strings:  
        # add first string to adjacency dict
        if len(visited_string) == 0:
            adjacency_dict[s] = []
            for i in range(len(s)):
                adjacency_dict[s].append([i+1, i+2, s[i]])
                n += 1
            visited_string.append(s)
            continue
        # if s is not the first string, and not in the visited_string, processing.
        if len(visited_string) > 0:
            most_string, most_overlap = get_most_overlap(s, visited_string)

            # if s not overlap with any visited strings
            if not most_overlap:
                adjacency_dict[s] = []
                adjacency_dict[s].append([1, n+1, s[0]])
                n += 1
                for i in range(1, len(s)):
                    adjacency_dict[s].append([n, n+1, s[i]])
                    n+=1
                visited_string.append(s)

            # if s overlap with any visited strings, get the most longest overlap string.
            if most_overlap:
                adjacency_dict[s] = []
                s_right = s[len(most_overlap):]

                adjacency_dict[s].extend(adjacency_dict[most_string][:len(most_overlap)])
                b = adjacency_dict[most_string][len(most_overlap)][0]
                adjacency_dict[s].append([b, n+1, s_right[0]])
                n+= 1
                for i in range(1, len(s_right)):
                    adjacency_dict[s].append([n, n+1, s_right[i]])
                    n+=1
                visited_string.append(s)
    return adjacency_dict

if __name__ == "__main__":
    with open("../data/rosalind_trie.txt", "r") as f:
        strings = [line.strip('\n') for line in f]

    strings = sorted(strings, key=lambda x:len(x), reverse=True)
    adjacency_dict = get_adjacency_dict(strings)
    
    # print(adjacency_dict)
    results = []
    for k, v in adjacency_dict.items():
        for b, e, s in v:
            if [b, e, s] not in results:
                results.append([b, e, s])
    for b, e, s in results:     
        print(b, e, s)
