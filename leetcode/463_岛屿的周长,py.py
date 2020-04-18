'''
@Author: your name
@Date: 2020-03-15 10:59:08
@LastEditTime: 2020-03-28 13:20:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\463_岛屿的周长,py.py
'''
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 10:58:36 2020

@author: haibao
"""
#遍历所有格子，每找到一块陆地，岛屿周长加4，同时检查该陆地格子，
#它的四周（水平垂直方向）每有一块陆地，周长减1（减少一条边）。如此这般，直至得到整个岛屿的周长。

class Solution:
    def islandPerimeter(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j]:
                    res+=4
                    if i>0 and grid[i-1][j]==1:
                        res-=2
                    if j>0 and grid[i][j-1]==1:
                        res-=2
        return res
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
a = Solution()
print(a.islandPerimeter(grid))       