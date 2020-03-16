# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 11:35:42 2020

@author: haibao
"""
class Solution:
    def constructArr(self, a):
        if not a: 
            return []
        n = len(a)
        L,R = [1]*n,[1]*n
        
        for i in range(1, n):
            L[i] = L[i - 1] * a[i - 1] 
        
        for j in reversed(range(n-1)):
            R[j] = R[j+1] * a[j+1]
        
        for i in range(n):
            L[i] = L[i]*R[i]
        return L

a = Solution()
print(a.constructArr([1,2,3,4,5]))