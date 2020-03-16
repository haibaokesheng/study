# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 22:14:45 2020

@author: haibao
2020.3.10 
给定一棵二叉树，你需要计算它的直径长度。
一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
"""
from binarytree import tree, bst, heap,build

values = [1,2,3,4,5]

root = build(values)
print(root)
class solution(): 
    def diameterOfBinaryTree(self,root):
        self.ans = 0
    
        def depth(root):
            if not root:
                 return 0
            l = depth(root.left)
            r = depth(root.right)
            '''每个结点都要去判断左子树+右子树的高度是否大于self.max，更新最大值'''
            self.ans = max(self.ans, l+r)
        
            # 返回的是高度
            return max(l, r) + 1
        depth(root)
        return self.ans
    
a = solution()
print(a.diameterOfBinaryTree(root))        