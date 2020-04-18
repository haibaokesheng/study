'''
@Author: your name
@Date: 2020-04-12 14:01:20
@LastEditTime: 2020-04-12 14:28:58
@LastEditors: Please set LastEditors
@Description: In User Settings Edi
@FilePath: \刷题人生\leetcode\257.二叉树的所有路径.py
'''
#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (62.36%)
# Likes:    239
# Dislikes: 0
# Total Accepted:    32K
# Total Submissions: 50.5K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 输入:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        ans = []
        def dfs(root, ans, path):
            if root.left == None and root.right == None:
                ans.append(path)
            if root.left != None:
                dfs(root.left, ans, path + '->' + str(root.left.val))
            if root.right != None:
                dfs(root.right, ans, path + '->' + str(root.right.val))
        
        dfs(root, ans, '' + str(root.val))
        
        return ans

        


# @lc code=end

