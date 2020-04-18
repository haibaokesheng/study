'''
@Author: your name
@Date: 2020-03-23 19:16:29
@LastEditTime: 2020-03-23 19:50:17
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\876.链表的中间结点.py
'''
#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast =slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
# @lc code=end

