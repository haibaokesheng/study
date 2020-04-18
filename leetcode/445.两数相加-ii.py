'''
@Author: your name
@Date: 2020-04-14 10:47:52
@LastEditTime: 2020-04-14 11:48:05
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\445.两数相加-ii.py
'''
#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (54.33%)
# Likes:    160
# Dislikes: 0
# Total Accepted:    22.7K
# Total Submissions: 40.4K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
# 
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 
# 
# 
# 进阶：
# 
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
# 
# 
# 
# 示例：
# 
# 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        ans = None
        carry = 0
        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            cur = a + b + carry
            carry = cur // 10
            cur %= 10
            curnode = ListNode(cur)
            curnode.next = ans
            ans = curnode

            #cur.next = temp
            #cur = cur.next  ########实际是将cur引用的位置从当前节点移动到下一节点
        return ans
        

        # 方法一：不修改原链表
        # 将链表转数字
        def node2num(node):
            num_str = []
            cur = node
            while cur:
                num_str.append(str(cur.val))
                cur = cur.next 
            return int(''.join(num_str))
        res = node2num(l1)+node2num(l2)
        # 将数字转链表
        Head = cur = ListNode(0)
        for c in str(res):
            val = int(c)
            cur.next = ListNode(val)
            cur = cur.next
        return Head.next 
# @lc code=end

