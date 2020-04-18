'''
@Author: your name
@Date: 2020-03-29 21:03:49
@LastEditTime: 2020-03-29 21:04:04
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\105.从前序与中序遍历序列构造二叉树.py
'''
#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (64.24%)
# Likes:    385
# Dislikes: 0
# Total Accepted:    54K
# Total Submissions: 83.6K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 根据一棵树的前序遍历与中序遍历构造二叉树。
# 
# 注意:
# 你可以假设树中没有重复的元素。
# 
# 例如，给出
# 
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 
# 返回如下的二叉树：
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
       if not preorder or  not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:1+index],inorder[:index])####下标是从0开始的
        root.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        return root
# @lc code=end

