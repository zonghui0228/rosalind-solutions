# Given: An integer money and an array Coins of positive integers.
# Return: The minimum number of coins with denominations Coins that changes money.
def CoinsChangeMoney(coins, money):
	result = []
	for i in coins:
		if money % i == 0:
			result.append(money / i)
	coins_seq = {}
	while money != 0:
		coins_seq[max(coins)] = money / max(coins)
		money = money % max(coins)
		coins.remove(max(coins))
	result.append(sum(coins_seq.values()))
	return min(result)


# coins = [1,3,5,6,7,10,15,24]
# money = 16960
# print CoinsChangeMoney(coins,money)
