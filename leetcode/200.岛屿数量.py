#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (47.13%)
# Likes:    485
# Dislikes: 0
# Total Accepted:    83.7K
# Total Submissions: 172.4K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 示例 1:
# 
# 输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入:
# 11000
# 11000
# 00100
# 00011
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
# 
# 
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # # BFS
        # count = 0
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if grid[row][col] == '1':  # 发现陆地
        #             count += 1  # 结果加1
        #             grid[row][col] = '0'  # 将其转为 ‘0’ 代表已经访问过
        #             # 对发现的陆地进行扩张即执行 BFS，将与其相邻的陆地都标记为已访问
        #             # 经典的 BFS 模板
        #             land_positions = collections.deque()
        #             land_positions.append([row, col])
        #             while land_positions:
        #                 x, y = land_positions.popleft()
        #                 for new_x, new_y in [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]:  # 进行四个方向的扩张
        #                     # 判断有效性
        #                     if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '1':
        #                         grid[new_x][new_y] = '0'  # 因为可由 BFS 访问到，代表同属一块岛，将其置 ‘0’ 代表已访问过
        #                         land_positions.append([new_x, new_y])
        # return count

        #DFS
        if not grid: 
            return 0
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return 
            grid[i][j] = '0'
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count
    
        

# @lc code=end

