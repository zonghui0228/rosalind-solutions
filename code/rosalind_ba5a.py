# ^_^ coding:utf-8 ^_^

"""
Find the Minimum Number of Coins Needed to Make Change
url: http://rosalind.info/problems/ba5a/

Given: An integer money and an array Coins of positive integers.
Return: The minimum number of coins with denominations Coins that changes money.
"""

def CoinsChangeMoney(coins, money):
    result = []
    for i in coins:
        if money % i == 0:
            result.append(money // i)
    coins_seq = {}
    while money != 0:
        coins_seq[max(coins)] = money // max(coins)
        money = money % max(coins)
        coins.remove(max(coins))
    result.append(sum(coins_seq.values()))
    return min(result)

if __name__ == "__main__":
    with open("../data/rosalind_ba5a.txt", "r") as f:
        money = int(f.readline().strip())
        coins = [int(l) for l in f.readline().strip().split(",")]
    print(CoinsChangeMoney(coins, money))