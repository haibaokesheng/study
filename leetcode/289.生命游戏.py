'''
@Author: your name
@Date: 2020-04-02 20:57:30
@LastEditTime: 2020-04-02 23:05:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\289.生命游戏.py
'''
#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#
# https://leetcode-cn.com/problems/game-of-life/description/
#
# algorithms
# Medium (69.15%)
# Likes:    163
# Dislikes: 0
# Total Accepted:    25.5K
# Total Submissions: 34.4K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# 根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
# 
# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0
# 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
# 
# 
# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
# 
# 
# 
# 根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
# 
# 
# 
# 示例：
# 
# 输入： 
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# 输出：
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
# 
# 
# 
# 进阶：
# 
# 
# 你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
# 本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？
# 
# 
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        def liveOrDead(board,i,j):
            ds = [(1, 1), (1, -1), (1, 0), (-1, 1), 
            (-1, 0), (-1, -1), (0, 1), (0, -1)]
            live_count = 0    
            for d  in ds:
                dx = i+d[0]
                dy = j+d[1]    
                if 0<=dx<row and 0<=dy<col:
                    if board[dx][dy]:
                        live_count+=1
            if board[i][j]: #live
                if live_count<2 or live_count>3 :
                    return 'dead'
                elif live_count==2 or live_count==3:
                    return 'live'
            else:# dead
                if live_count==3:
                    return 'live'

        board_next = copy.deepcopy(board)
        for i in range(row):
            for j in range(col):
                status = liveOrDead(board,i,j)
                if status == 'live':
                    board_next[i][j]=1
                elif status == 'dead':
                    board_next[i][j]=0
        for i in range(row):
            for j in range(col):
                board[i][j] = board_next[i][j]
        
        
        #卷积算法            
        # import numpy as np
        # r,c=len(board),len(board[0])
        # #下面两行做zero padding
        # board_exp = np.array([[0 for _ in range(c+2)] for _ in range(r+2)])
        # board_exp[1:1+r,1:1+c] = np.array(board)
        # #设置卷积核
        # kernel=np.array([[1,1,1],[1,0,1],[1,1,1]])
        # #开始卷积
        # for i in range(1,r+1):
        #     for j in range(1,c+1):
        #         #统计细胞周围8个位置的状态
        #         temp_sum = np.sum(kernel*board_exp[i-1:i+2,j-1:j+2])
        #         #按照题目规则进行判断
        #         if board_exp[i,j]: #live
        #             if temp_sum<2 or temp_sum>3:  #1 3
        #                 board[i-1][j-1]=0
        #         else:             # dead
        #             if temp_sum==3:   #4
        #                 board[i-1][j-1]=1       

        
# @lc code=end

