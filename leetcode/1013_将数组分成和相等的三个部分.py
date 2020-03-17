# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:07:41 2020

@author: haibao
2020.3.11
"""
#给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        he = sum(A)
        if he%3:
            return False
        avg = he/3
        temp = 0
        count = 0
        for i in A:
            temp+=i
            if temp == avg:
                count+=1
                temp = 0
        return count >= 3

A = [0,2,1,-6,6,-7,9,1,2,0,1]
A = [10,-10,10,-10,10,-10,10,-10]  #[10,-10],[10,-10,10,-10],[10,-10]
a = Solution()
print(a.canThreePartsEqualSum(A))



