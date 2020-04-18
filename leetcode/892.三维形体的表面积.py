'''
@Author: your name
@Date: 2020-03-25 19:45:33
@LastEditTime: 2020-03-25 20:32:41
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\892.三维形体的表面积.py
'''
#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#
# https://leetcode-cn.com/problems/surface-area-of-3d-shapes/description/
#
# algorithms
# Easy (55.77%)
# Likes:    91
# Dislikes: 0
# Total Accepted:    20.5K
# Total Submissions: 32.2K
# Testcase Example:  '[[2]]'
#
# 在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
# 
# 每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
# 
# 请你返回最终形体的表面积。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：[[2]]
# 输出：10
# 
# 
# 示例 2：
# 
# 输入：[[1,2],[3,4]]
# 输出：34
# 
# 
# 示例 3：
# 
# 输入：[[1,0],[0,2]]
# 输出：16
# 
# 
# 示例 4：
# 
# 输入：[[1,1,1],[1,0,1],[1,1,1]]
# 输出：32
# 
# 
# 示例 5：
# 
# 输入：[[2,2,2],[2,1,2],[2,2,2]]
# 输出：46
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 50
# 0 <= grid[i][j] <= 50
# 
# 
#

# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    ans += grid[i][j] * 4 + 2
                if i > 0:
                    ans -= 2 * min(grid[i][j], grid[i - 1][j])
                if j > 0:
                    ans -= 2 * min(grid[i][j], grid[i][j - 1])
        return ans
        
# @lc code=end

