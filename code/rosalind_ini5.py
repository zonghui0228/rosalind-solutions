# ^_^ coding:utf-8 ^_^

"""
Working with Files
url: http://rosalind.info/problems/ini5/

Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
"""

def even_line(lines):
    return [lines[i] for i in range(len(lines)) if i%2==1]

if __name__ == "__main__":
    with open("../data/rosalind_ini5.txt", "r") as f:
        lines = f.readlines()
    even_lines = even_line(lines)
    print("".join(even_lines))