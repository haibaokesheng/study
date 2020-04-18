'''
@Author: your name
@Date: 2020-04-14 21:34:00
@LastEditTime: 2020-04-14 21:34:24
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\102.二叉树的层次遍历.py
'''
#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (60.99%)
# Likes:    445
# Dislikes: 0
# Total Accepted:    103.8K
# Total Submissions: 168.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 
# 
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        quene = [root]
        while(quene):
            level = []
            size = len(quene)
            for  _ in range(size):################
                node = quene.pop(0)
                if node.left:
                    quene.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    quene.append(node.right)
                    level.append(node.right.val)
            if level:
                res.append(level)
        #print(res)
        return res
# @lc code=end

