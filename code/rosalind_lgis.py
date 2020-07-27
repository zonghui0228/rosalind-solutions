# coding:utf-8

"""
Longest Increasing Subsequence
url: http://rosalind.info/problems/lgis/

Given: A positive integer n≤10000 followed by a permutation π of length n.
Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
"""

def LIS(nums, n):
    dp = [] # 记录到每个节点时LIS的长度，int
    dp_list = [] # 记录到每个节点时LIS的内容, list

    for i in range(n):
        dp.append(1)
        dp_list.append([nums[i]])
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                if len(dp_list[i]) <= len(dp_list[j]):
                    dp_list[i] = dp_list[j] + [nums[i]]
    # print(dp, dp_list)
    print(max(dp), dp_list[dp.index(max(dp))])
    return dp, dp_list

# Longest Decreasing Subsequence
def LDS(nums, n):
    dp = [] # 记录到每个节点时LIS的长度，int
    dp_list = [] # 记录到每个节点时LIS的内容, list

    for i in range(n):
        dp.append(1)
        dp_list.append([nums[i]])
        for j in range(i):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                if len(dp_list[i]) <= len(dp_list[j]):
                    dp_list[i] = dp_list[j] + [nums[i]]
    # print(dp, dp_list)
    print(max(dp), dp_list[dp.index(max(dp))])
    return dp, dp_list

if __name__ == "__main__":
    with open("../data/rosalind_lgis.txt", "r") as f:
        n = int(f.readline().strip())
        nums = [int(i) for i in f.readline().strip().split(" ")]

    LIS(nums, n)
    LDS(nums, n)
    