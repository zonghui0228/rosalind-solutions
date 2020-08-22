# ^_^ coding:utf-8 ^_^

"""
Strings and Lists
url: http://rosalind.info/problems/ini3/

Given: A string s of length at most 200 letters and four integers a, b, c and d.
Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
"""

def string_slice(s, a, b, c, d):
    return s[a:b+1], s[c:d+1]

if __name__ == "__main__":
    with open("../data/rosalind_ini3.txt", "r") as f:
        s = f.readline().strip()
        a, b, c, d = map(int, f.readline().strip().split())
    s1, s2 = string_slice(s, a, b, c, d)
    print(s1, s2)
