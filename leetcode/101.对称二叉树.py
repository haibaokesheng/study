'''
@Author: your name
@Date: 2020-04-12 11:51:04
@LastEditTime: 2020-04-13 14:31:57
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\101.对称二叉树.py
'''
#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (50.27%)
# Likes:    716
# Dislikes: 0
# Total Accepted:    120.9K
# Total Submissions: 238.2K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# 进阶：
# 
# 你可以运用递归和迭代两种方法解决这个问题吗？
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
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def isame(p,q):
            if not p and not q: #都为空的话，显然对称
                return True
            if not p or not q:  #一个为空，一个非空，显然不对称
                return False
            if p.val != q.val:
                return False
            return isame(p.left,q.right) and isame(p.right,q.left)
            
        return isame(root.left,root.right)
        
# @lc code=end

