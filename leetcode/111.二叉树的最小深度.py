#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (41.65%)
# Likes:    243
# Dislikes: 0
# Total Accepted:    66.8K
# Total Submissions: 158.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
# 
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最小深度  2.
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
    def minDepth(self, root: TreeNode) -> int:
        ''' bfs'''
        if not root:
            return 0
        quene = [root]
        depth = 1
        while(quene):
            for _ in range(len(quene)):
                node = quene.pop(0)
                if  not node.left and not node.right:
                    return depth
                if node.left:
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)
            depth+=1
        return  depth
# @lc code=end

