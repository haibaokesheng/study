#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (46.16%)
# Likes:    262
# Dislikes: 0
# Total Accepted:    43.4K
# Total Submissions: 91.6K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
# 
# 示例 1:
# 
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 
# 
# 示例 2:
# 
# 输入: 1->1->1->2->3
# 输出: 2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        cur = head
        pre.next = cur
        while cur and cur.next:
            if cur.next.val!=cur.val:
                pre = cur
            else:
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                pre.next = cur.next
            cur = cur.next
        return dummy.next
# @lc code=end

