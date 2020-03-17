# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 09:03:10 2020

@author: haibao
2020.3.15 leetcode每日一题 时间复杂度O(R*C)R是网格的行数，C是列数
"""

class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
     
        def dfs(i,j):
            
            if i<0 or i==m or j<0 or j==n or not grid[i][j]:
                return 0  #递归截至条件
            if grid[i][j]:
                grid[i][j]=0
                return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j-1)+dfs(i,j+1)
         
        res = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    res = max(res,dfs(x,y))
        return res
gird = [[1,0,0],[1,0,0],[1,0,0]]
a = Solution()
print(a.maxAreaOfIsland(gird))               