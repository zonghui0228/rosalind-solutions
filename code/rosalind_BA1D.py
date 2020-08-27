# ^_^ coding:utf-8 ^_^

"""
Find All Occurrences of a Pattern in a String
url: http://rosalind.info/problems/ba1d/

Given: Strings Pattern and Genome.
Return: All starting positions in Genome where Pattern appears as a substring. Use 0-based indexing.
"""

def positions_pattern(pattern, text):
    positions = []
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            positions.append(i)
            print(i, end= " ")
    print()
    return positions

if __name__ == "__main__":
    with open("../data/rosalind_ba1d.txt", "r") as f:
        pattern = f.readline().strip()
        text = f.readline().strip()
    positions_pattern(pattern, text)