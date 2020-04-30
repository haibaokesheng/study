#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (60.00%)
# Likes:    966
# Dislikes: 0
# Total Accepted:    237.5K
# Total Submissions: 388K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        迭代
        '''
        # 类似归并排序中的合并过程
        # 建立一个头结点
        new_head = ListNode(None)
        # 返回的节点
        cur = new_head
        # 开始遍历
        while l1 and l2:
            # 如果l1的数值比较小
            if l1.val < l2.val:
                # new_head节点后面接l1
                new_head.next = l1
                # 因为new_head节点后面接l1，所以new_head节点要后面移动一位
                new_head = new_head.next
                l1 = l1.next
            else:
                new_head.next = l2
                new_head = new_head.next
                l2 = l2.next
        # 如果l1、l2不等长度，那么在new_head后面接入较长的还剩下的链表头结点
        if l1 or l2:
            new_head.next = l1 or l2
        # 返回
        return cur.next


        '''
        递归
        '''
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val<l2.val:
            mergeHead = l1
            mergeHead.next = self.mergeTwoLists(l1.next,l2)
        else:
            mergeHead = l2
            mergeHead.next = self.mergeTwoLists(l1,l2.next)
        return mergeHead
# @lc code=end

