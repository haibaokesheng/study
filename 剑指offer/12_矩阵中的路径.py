# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 22:19:25 2020

@author: haibao
"""
#可以遍历整个网格，只要符合单词的第一个字母，就开始backtrack递归，
#按四个方向查，如果在边界内，且没有走过，就走下去，直到找到单词为止，
#找到的话就不用再找其他可能的入口了，直接返回true；没有的话就按下一个入口位置开始向四周找

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        len_1 = len(board)
        len_2 = len(board[0])
        len_s = len(word)
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[0] * len_2 for _ in range(len_1)]
        print(visited)
        def track_back(x, y, ind):
            #x,y表示当前访问的数组boardboard的位置索引。ind表示正在和word匹配的位置。
            if ind == len_s:#递归终止条件
                return True
            if x < 0 or x >= len_1 or y < 0 or y >= len_2 or visited[x][y] or board[x][y] != word[ind]:
                return False
            visited[x][y] = 1
            for (i, j) in direction:
                if track_back(x + i, y + j, ind + 1):
                    return True
            visited[x][y] = 0 # 若查找失败，则将当前访问状态手动置为0
            return False
        
        for x in range(len_1):
            for y in range(len_2):
                if track_back(x, y, 0):
                    return True
        return False

a = Solution()
board = [['a','b','t','g'],
         ['c','f','c','s'],
         ['j','d','e','h']]
word = "bfce"
print(a.exist(board,word))