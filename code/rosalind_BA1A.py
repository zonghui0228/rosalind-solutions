# ^_^ coding:utf-8 ^_^

"""
Compute the Number of Times a Pattern Appears in a Text
url:http://rosalind.info/problems/ba1a/

Given: {DNA strings}} Text and Pattern.
Return: Count(Text, Pattern).
"""

def PatternCount(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

if __name__ == "__main__":
    with open("../data/rosalind_ba1a.txt", "r") as f:
        text = f.readline().strip()
        pattern = f.readline().strip()
    print(PatternCount(text, pattern))
