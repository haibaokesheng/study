'''
@Author: your name
@Date: 2020-04-12 11:13:18
@LastEditTime: 2020-04-12 11:19:18
@LastEditors: Please set LastEditors
@Description: In User Settings Edi
@FilePath: \刷题人生\leetcode\104.二叉树的最大深度.py
'''
#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (72.35%)
# Likes:    502
# Dislikes: 0
# Total Accepted:    155.5K
# Total Submissions: 213.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回它的最大深度 3 。
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''解法一 DFS '''
        # dfs
        # if not root:
        #    return 0
        #leftMaxDepth = self.maxDepth(root.left)
        #rightMaxDepth = self.maxDepth(root.right)
        # return max(leftMaxDepth,rightMaxDepth)+1
        # return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

        # return 0 if not root else max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        # if not root:
        #     return 0
        # bfs
        '''解法二 BFS  '''
        if not root:
            return 0
        res = 0
        quene = [root]
        while quene:
            for _ in range(len(quene)):
                node = quene.pop(0)
                if node.right:
                    quene.append(node.right)
                if node.left:
                    quene.append(node.left)
            res += 1
        return res

# @lc code=end
