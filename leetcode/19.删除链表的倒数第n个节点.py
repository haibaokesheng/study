#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (37.71%)
# Likes:    783
# Dislikes: 0
# Total Accepted:    153.8K
# Total Submissions: 401.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 
# 示例：
# 
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 
# 
# 说明：
# 
# 给定的 n 保证是有效的。
# 
# 进阶：
# 
# 你能尝试使用一趟扫描实现吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 思路：双指针法。
        slow = fast = head
        for _ in range(n):          # 先让fast走n步
            fast = fast.next
        if fast == None:            # 若走了n步后为None，则表明删除的为head节点
            return head.next
        
        while fast.next != None:    # slow和fast同时往前走
            slow = slow.next        # 当fast走到头时，second即是要删除节点的前一个节点位置
            fast = fast.next
        slow.next = slow.next.next  # 删除该节点
        return head
# @lc code=end

