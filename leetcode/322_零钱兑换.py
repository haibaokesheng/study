# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:36:13 2020

@author: haibao
"""

coins = [1,2,5]
amount = 11

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [0 for _ in range(amount + 1)]
        
        for i in range(1, amount + 1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, res[i - c] + 1)
            res[i] = cost
        
        if res[amount] == float('inf'):
            return -1
        else:
            return res[amount]
a = Solution()
print(a.coinChange(coins,amount))        