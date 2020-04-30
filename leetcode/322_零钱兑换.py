# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:36:13 2020

@author: haibao
"""

coins = [1,2,5]
amount = 11
"""
题目求的值为 f(11)，第一次选择硬币时我们有三种选择。
假设我们取面额为 1 的硬币，那么接下来需要凑齐的总金额变为 11 - 1 = 10，
即 f(11) = f(10) + 1，这里的 +1 就是我们取出的面额为 1 的硬币。
同理，如果取面额为 2 或面额为 5 的硬币可以得到：
f(11) = f(9) + 1
f(11) = f(6) + 1
所以：f(11) = min(f(10), f(9), f(6)) + 1
自下而上的DP 
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0 for _ in range(amount + 1)]
        
        for i in range(1, amount + 1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, dp[i - c] + 1)
            dp[i] = cost
        
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
a = Solution()
print(a.coinChange(coins,amount))        