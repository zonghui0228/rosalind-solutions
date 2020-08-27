# ^_^ coding:utf-8 ^_^

"""
Find the Most Frequent Words in a String
url: http://rosalind.info/problems/ba1b/

Given: A DNA string Text and an integer k.
Return: All most frequent k-mers in Text (in any order).
"""

def FrequentWords(text, k):
    word_count = {}
    for i in range(len(text)-k+1):
        if text[i:i+k] not in word_count:
            word_count[text[i:i+k]] = 0
        word_count[text[i:i+k]] += 1
    frequent_count = max(word_count.values())
    for k,v in word_count.items():
        if v==frequent_count:
            print(k, end=" ")
    print()
    return word_count
    
if __name__ == "__main__":
    with open("../data/rosalind_ba1b.txt", "r") as f:
        text = f.readline().strip()
        k = int(f.readline().strip())
    FrequentWords(text, k)