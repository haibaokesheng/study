'''
@Author: your name
@Date: 2020-03-29 14:22:12
@LastEditTime: 2020-03-29 15:27:49
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\1162.地图分析.py
'''
#
# @lc app=leetcode.cn id=1162 lang=python3
#
# [1162] 地图分析
#
# https://leetcode-cn.com/problems/as-far-from-land-as-possible/description/
#
# algorithms
# Medium (38.27%)
# Likes:    54
# Dislikes: 0
# Total Accepted:    12.1K
# Total Submissions: 28.3K
# Testcase Example:  '[[1,0,1],[0,0,0],[1,0,1]]'
#
# 你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1
# 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。
# 
# 我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 -
# x1| + |y0 - y1| 。
# 
# 如果我们的地图上只有陆地或者海洋，请返回 -1。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[[1,0,1],[0,0,0],[1,0,1]]
# 输出：2
# 解释： 
# 海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：[[1,0,0],[0,0,0],[0,0,0]]
# 输出：4
# 解释： 
# 海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length == grid[0].length <= 100
# grid[i][j] 不是 0 就是 1
# 
# 
#

# @lc code=start
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        steps = -1
        queue = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        if len(queue) == 0 or len(queue) == n ** 2:
             return steps
        
        while queue :
            for _ in range(len(queue)): 
                x, y = queue.pop(0)
                for xi, yj in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if xi >= 0 and xi < n and yj >= 0 and yj < n and grid[xi][yj] == 0:
                        queue.append((xi, yj))
                        grid[xi][yj] = -1
            steps += 1
                
        return steps

      

        
        
# @lc code=end

