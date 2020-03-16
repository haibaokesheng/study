# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 17:44:48 2020

@author: haibao
"""
# and 的短路特性
class Solution:
    def sumNums(self, n) -> int:
        print(n)
        return n and self.sumNums(n-1)+n
a = Solution()
print(a.sumNums(6))