#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (70.36%)
# Likes:    440
# Dislikes: 0
# Total Accepted:    129.9K
# Total Submissions: 183.6K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 输出: [1,3,2]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''写法一'''
        # res = []
        # def cur(root):
        #     if not root:
        #         return
        #     cur(root.left)
        #     res.append(root.val)
        #     cur(root.right)
        # cur(root)
        # return res
        '''写法二'''
        def helper(root):
            return helper(root.left) + [root.val] + helper(root.right) if root else []
        return helper(root)
    '''写法三'''
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     stack,rst = [root],[]
    #     while stack:
    #         i = stack.pop()
    #         if isinstance(i,TreeNode):
    #             stack.extend([i.right,i.val,i.left])
    #         elif isinstance(i,int):
    #             rst.append(i)
    #     return rst

  
# @lc code=end


