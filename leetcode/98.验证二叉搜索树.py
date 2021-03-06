#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (29.11%)
# Likes:    552
# Dislikes: 0
# Total Accepted:    106.9K
# Total Submissions: 349.1K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 
# 假设一个二叉搜索树具有如下特征：
# 
# 
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 示例 1:
# 
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
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
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, min_val, max_val):
            if not node:  # 边界条件，如果node为空肯定是二叉搜索树
                return True
            if not min_val < node.val < max_val:  # 如果当前节点超出上下界范围，肯定不是
                return False
            # 走到下面这步说明已经满足了如题所述的二叉搜索树的前两个条件
            # 那么只需要递归判断当前节点的左右子树是否同时是二叉搜索树即可
            if dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val):
                return True
            else:
                return False
        return dfs(root, float('-inf'), float('inf')) # 对于根节点，它的上下限为无穷大和无无穷小
        
# @lc code=end

