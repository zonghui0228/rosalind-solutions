# ^_^ coding:utf-8 ^_^

"""
Wobble Bonding and RNA Secondary Structures
url: http://rosalind.info/problems/rnas/

Given: An RNA string s (of length at most 200 bp).
Return: The total number of distinct valid matchings of basepair edges in the bonding graph of s. Assume that wobble base pairing is allowed.
"""

def _get_bonding_graph(s, wobble_memo):
    if len(s) <= 3:
        return 1
    if s in wobble_memo:
    	return wobble_memo[s]
    n = _get_bonding_graph(s[1:], wobble_memo)
    for i in range(4, len(s)):
            if (s[0], s[i]) in [("A", "U"), ("U", "A"), ("C", "G"), ("G", "C"), ("U", "G"), ("G", "U")]:
                n += _get_bonding_graph(s[1:i], wobble_memo) * _get_bonding_graph(s[i+1:], wobble_memo)
    wobble_memo[s] = n
    return n


if __name__ == "__main__":
    # test
    s = "CGAUGCUAG" # n=12
    s = "AUGCUAGUACGGAGCGAGUCUAGCGAGCGAUGUCGUGAGUACUAUAUAUGCGCAUAAGCCACGU" # n = 284850219977421
    print(s)
    wobble_memo = {} # Memorize calculated Wobble Bonding
    n = _get_bonding_graph(s, wobble_memo)
    print(n)

    # load data
    # with open("../data/rosalind_rnas.txt", "r") as f:
    #     s = f.readline().strip()
    #     print(s)
    #     wobble_memo = {} # Memorize calculated Wobble Bonding
    #     n = _get_bonding_graph(s, wobble_memo)
    #     print(n)
    print("done!")

