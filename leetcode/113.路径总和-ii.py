'''
@Author: your name
@Date: 2020-04-12 14:34:16
@LastEditTime: 2020-04-12 19:14:19
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\113.路径总和-ii.py
'''
#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (58.92%)
# Likes:    203
# Dislikes: 0
# Total Accepted:    40.9K
# Total Submissions: 69.2K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
# 
# 
# 返回:
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        def find(root,sum,path):
            if not root:
                return res
            if not root.left and not root.right :#叶子节点
                if sum-root.val==0:
                    path +=[root.val]
                    res.append(path)
                    
            find(root.left,sum-root.val,path+[root.val])
            find(root.right,sum-root.val,path+[root.val])
        find(root,sum,[])
        return res
# @lc code=end

